import pandas as pd


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
    global teamsList
    global driversList
    global numTeams
    global driverAssignment
    numTeams = input("How many teams would you like to enter? ")
    for i in range(int(numTeams)):
        id = int(input("Please enter Constructor ID: ")) - 1
        teamsList.append(id)
        print(constructors.at[id, "name"])

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
        global teamsList
        global driversList
        global numTeams
        global driverAssignment
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

        numTeams = lines - 1
    return driverAssignment
    # simulate()


def randomSetup():
    print('TODO')
    from random import randrange
    global teamsList
    global driversList
    global numTeams
    global driverAssignment

    numTeams = input("How many teams would you like to enter? ")

    for i in range(int(numTeams)):
        id = randrange(214)
        teamsList.append(id)
        # print(constructors.at[id, "name"])

    for i in range(int(numTeams)):
        print("Constructor:", constructors.at[teamsList[i], "name"])

        id1 = randrange(850)
        driversList.append(id1)
        print(drivers.at[id1, "forename"], drivers.at[id1, "surname"])

        id2 = randrange(850)
        driversList.append(id2)
        print(drivers.at[id2, "forename"], drivers.at[id2, "surname"])
        print('')
        driverAssignment[teamsList[i]] = [id1, id2]

    circuitID = randrange(77)
    print('')
    print(circuits.at[circuitID, "name"] + ',', circuits.at[circuitID, "country"])
    # simulate()


def simulate():

    # display track
    # generate int(numTracks)*2 circles
    # colour in team colours
    # assign driver label

    # qualify
    # print grid
    printGrid(quali())

    # race
    # print results
    printGrid(race())

    # ????


def printGrid(resultsDict):
    p = 1
    global teamsList
    global driversList
    global numTeams
    global driverAssignment
    for key in resultsDict:

        # print('DEBUG', resultsDict)
        # print('DEBUG', key)
        print('P' + (str(p)))
        p = p + 1
        print(drivers.at[key - 1, "forename"], drivers.at[key - 1, "surname"])

        for k, v in driverAssignment.items():
            if key - 1 in v:
                print(constructors.at[k, "name"])
        # index = [k for k, v in driverAssignment.items() if i in v]
        # print(constructors.at[index[0], "name"])

        print('')


def quali():
    global teamsList
    global driversList
    global numTeams
    global driverAssignment
    qualiPerformance = {}
    for i in range(int(numTeams) * 2):  # for every driver on grid
        # read average quali from csv
        index = drivers.at[driversList[i], "driverId"]
        qualiPerformance[index] = averageQuali.at[index - 1, "averageQuali"]

        # print('DEBUG', drivers.at[driversList[i], "surname"], averageQuali.at[index-1, "averageQuali"])
    # sort dictionary by performance
    qualiPerformance = sorted(qualiPerformance, key=lambda i: int(qualiPerformance[i]))
    # TODO implement a random tiebreak
    # TODO add some constructor performance
    print("")
    print("QUALIFYING RESULTS")
    print("")
    return qualiPerformance


def race():
    global teamsList
    global driversList
    global numTeams
    global driverAssignment
    # ????
    # boring way of doing it:
    # TODO add some input from quali
    # TODO add some constructor performance

    racePerformance = {}
    for i in range(int(numTeams) * 2):  # for every driver on grid
        # read average finish from csv
        # TODO fix
        index = drivers.at[driversList[i], "driverId"]
        racePerformance[index] = averageFinish.at[index - 1, "averageFinish"]
    # sort dictionary by performance
    racePerformance = sorted(racePerformance, key=lambda i: int(racePerformance[i]))
    # TODO implement a random tiebreak
    print("")
    print("RACE RESULTS")
    print("")
    return racePerformance


if __name__ == '__main__':
    drivers = pd.read_csv("..\data\drivers.csv",
                          usecols=["driverId", "driverRef", "number", "code", "forename", "surname"])
    circuits = pd.read_csv("..\data\circuits.csv", usecols=["circuitId", "circuitRef", "name", "location", "country"])
    races = pd.read_csv("..\data\\races.csv", usecols=["raceId", "year", "round", "circuitId", "name"])
    results = pd.read_csv("..\data\\results.csv",
                          usecols=["resultId", "raceId", "driverId", "constructorId", "number", "grid", "position"])
    constructors = pd.read_csv("..\data\constructors.csv", usecols=["constructorId", "constructorRef", "name"])
    averageFinish = pd.read_csv("..\data\\average_finish.csv", usecols=["driverId", "averageFinish"])
    averageQuali = pd.read_csv("..\data\\average_quali.csv", usecols=["driverId", "averageQuali"])

    global numTeams
    global teamsList
    global driversList
    global driverAssignment


    # TODO get grid from season
    # TODO random grid
    # TODO random between certain dates?



    menu()
    # manualSetup()
