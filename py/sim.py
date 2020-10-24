import pandas as pd

drivers = pd.read_csv("..\data\drivers.csv", usecols=["driverId", "driverRef", "number", "code", "forename", "surname"])
circuits = pd.read_csv("..\data\circuits.csv", usecols=["circuitId", "circuitRef", "name", "location", "country"])
races = pd.read_csv("..\data\\races.csv", usecols=["raceId", "year", "round", "circuitId", "name"])
results = pd.read_csv("..\data\\results.csv", usecols=["resultId", "raceId", "driverId", "constructorId", "number", "grid", "position"])
constructors = pd.read_csv("..\data\constructors.csv", usecols=["constructorId", "constructorRef", "name"])
averageFinish = pd.read_csv("..\data\\average_finish.csv", usecols=["driverId", "averageFinish"])
averageQuali = pd.read_csv("..\data\\average_quali.csv", usecols=["driverId", "averageQuali"])
averageConstructorQuali = pd.read_csv("..\data\\constructor_average_quali.csv", usecols=["constructorId", "averageQuali"])
averageConstructorFinish = pd.read_csv("..\data\\constructor_average_finish.csv", usecols=["constructorId", "averageFinish"])

global numTeams
teamsList = []
driversList = []
driverAssignment = {}


def menu():
    inp = 0
    print("Welcome to the F1 Sim!")
    print("Main Menu")
    print("Manual setup - 1")
    print("Read from file - 2")
    print("Random grid - 3")
    inp = input("Please select mode: ")

    if inp == "1":
        manualSetup()
    if inp == "2":
        fileSetup()
    if inp == "3":
        randomSetup()


def manualSetup():
    global numTeams
    numTeams = input("How many teams would you like to enter? ")
    for i in range(int(numTeams)):
        team = int(input("Please enter Constructor ID: ")) - 1
        teamsList.append(team)
        print(constructors.at[team, "name"])

    for i in range(int(numTeams)):
        print("Constructor:", constructors.at[teamsList[i], "name"])

        id1 = int(input("Please enter Driver 1 ID: ")) - 1
        driversList.append(id1)
        print(drivers.at[id1, "forename"], drivers.at[id1, "surname"])

        id2 = int(input("Please enter Driver 2 ID: ")) - 1
        driversList.append(id2)
        print(drivers.at[id2, "forename"], drivers.at[id2, "surname"])

        driverAssignment[teamsList[i]] = [id1, id2]

    circuitID = int(input("Please enter Circuit ID: ")) - 1
    print('')
    print(circuits.at[circuitID, "name"] + ',', circuits.at[circuitID, "country"])
    simulate()


def fileSetup():
    print('')
    import csv
    with open('..\data\config.csv', 'r') as csvfile:
        config = list(csv.reader(csvfile, delimiter=','))

        lines = 0
        for row in config:
            if lines == 0:
                circuitID = int(row[0]) - 1
            else:
                team = int(row[0]) - 1
                teamsList.append(team)

                driver1 = int(row[1]) - 1
                driversList.append(driver1)

                driver2 = int(row[2]) - 1
                driversList.append(driver2)

                driverAssignment[team] = [driver1, driver2]
            lines += 1
        print(circuits.at[circuitID, "name"] + ',', circuits.at[circuitID, "country"])
        global numTeams
        numTeams = lines - 1

    simulate()


def randomSetup():
    from random import randrange
    global numTeams
    numTeams = input("How many teams would you like to enter? ")

    for i in range(int(numTeams)):
        team = randrange(213)
        teamsList.append(team)

    for i in range(int(numTeams)):
        print("Constructor:", constructors.at[teamsList[i], "name"])

        id1 = randrange(849)
        driversList.append(id1)
        print(drivers.at[id1, "forename"], drivers.at[id1, "surname"])

        id2 = randrange(849)
        driversList.append(id2)
        print(drivers.at[id2, "forename"], drivers.at[id2, "surname"])
        print('')
        driverAssignment[teamsList[i]] = [id1, id2]

    circuitID = randrange(76)
    print('')
    print(circuits.at[circuitID, "name"] + ',', circuits.at[circuitID, "country"])
    simulate()


def simulate():
    # TODO make it look pretty :(

    input("Press enter to simulate qualifying.")
    # qualify
    # print grid
    printGrid(quali())

    input("Press enter to simulate race.")
    # race
    # print results
    printGrid(race())


def printGrid(resultsDict):
    p = 1
    for key in resultsDict:

        print('P' + (str(p)))
        p = p + 1
        print(drivers.at[key - 1, "forename"], drivers.at[key - 1, "surname"])

        for k, v in driverAssignment.items():
            if key - 1 in v:
                print(constructors.at[k, "name"])

        print('')


def identifyTeam(index):
    found = False
    # TODO there's some weird issue with the random setup misidentifying some drivers here, maybe to do with the driver ids in the csv
    for k, v in driverAssignment.items():
        if index - 1 in v:
            constructorId = constructors.at[k, "constructorId"]
            found = True
            break

    # trying to catch that weird error from the todo on 171
    if not found:
        constructorId = 1

    return constructorId


def quali():
    qualiPerformance = {}
    for i in range(int(numTeams) * 2):  # for every driver on grid
        # read average quali from csv
        index = drivers.at[driversList[i], "driverId"]

        constructorId = identifyTeam(index)
        # weighted by car performance
        average = ((averageQuali.at[index - 1, "averageQuali"] * 0.25) + (
                averageConstructorQuali.at[constructorId-1, "averageQuali"] * 0.75))

        qualiPerformance[index] = average

    # sort dictionary by performance
    qualiPerformance = sorted(qualiPerformance, key=lambda i: int(qualiPerformance[i]))

    print("")
    print("QUALIFYING RESULTS")
    print("")
    return qualiPerformance


def race():
    # TODO add some input from quali
    # TODO add a stat for positions gained/lost from quali

    racePerformance = {}
    for i in range(int(numTeams) * 2):  # for every driver on grid
        # read average finish from csvs
        index = drivers.at[driversList[i], "driverId"]
        constructorId = identifyTeam(index)

        # not sure if this does what I want it to
        # essentially the car/team is responsible for 75% of the results
        average = ((averageFinish.at[index - 1, "averageFinish"] * 0.25) + (
                averageConstructorFinish.at[constructorId-1, "averageFinish"] * 0.75))
        racePerformance[index] = average

    # sort dictionary by performance
    racePerformance = sorted(racePerformance, key=lambda i: int(racePerformance[i]))

    print("")
    print("RACE RESULTS")
    print("")
    return racePerformance


menu()
