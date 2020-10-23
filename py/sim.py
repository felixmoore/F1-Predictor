import pandas as pd

drivers = pd.read_csv("..\data\drivers.csv", usecols=["driverId", "driverRef", "number", "code", "forename", "surname"])
circuits = pd.read_csv("..\data\circuits.csv", usecols=["circuitId", "circuitRef", "name", "location", "country"])
races = pd.read_csv("..\data\\races.csv", usecols=["raceId", "year", "round", "circuitId", "name"])
results = pd.read_csv("..\data\\results.csv",
                      usecols=["resultId", "raceId", "driverId", "constructorId", "number", "grid", "position"])
constructors = pd.read_csv("..\data\constructors.csv", usecols=["constructorId", "constructorRef", "name"])
averageFinish = pd.read_csv("..\data\\average_finish.csv", usecols=["driverId", "averageFinish"])
averageQuali = pd.read_csv("..\data\\average_quali.csv", usecols=["driverId", "averageQuali"])

numTeams = input("How many teams would you like to enter? ")
teamsList = []
driversList = []
driverAssignment = {}


# TODO get grid from file
# TODO get grid from season
# TODO random grid
    #TODO random between certain dates?
# TODO menu

def setup():
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
    print(circuits.at[circuitID, "name"] + ',', circuits.at[circuitID, "country"])


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
    for key in resultsDict:

       # print('DEBUG', resultsDict)
       # print('DEBUG', key)
        print('P' + (str(p)))
        p = p+1
        print(drivers.at[key-1, "forename"], drivers.at[key-1, "surname"])

        for k, v in driverAssignment.items():
            if key-1 in v:
                print(constructors.at[k, "name"])
        # index = [k for k, v in driverAssignment.items() if i in v]
        # print(constructors.at[index[0], "name"])

        print('')


def quali():
    qualiPerformance = {}
    for i in range(int(numTeams) * 2):  # for every driver on grid
        # read average quali from csv
        index = drivers.at[driversList[i], "driverId"]
        qualiPerformance[index] = averageQuali.at[index, "averageQuali"]
    # sort dictionary by performance
    qualiPerformance = sorted(qualiPerformance, key=lambda i: int(qualiPerformance[i]))
    #TODO implement a random tiebreak
    #TODO add some constructor performance
    print("")
    print("QUALIFYING RESULTS")
    print("")
    return qualiPerformance


def race():
    # ????
    # boring way of doing it:
    # TODO add some input from quali
    # TODO add some constructor performance

    racePerformance = {}
    for i in range(int(numTeams) * 2):  # for every driver on grid
        # read average finish from csv
        # TODO fix
        index = drivers.at[driversList[i], "driverId"]
        racePerformance[index] = averageFinish.at[index, "averageFinish"]
    # sort dictionary by performance
    racePerformance = sorted(racePerformance, key=lambda i: int(racePerformance[i]))
    # TODO implement a random tiebreak
    print("")
    print("RACE RESULTS")
    print("")
    return racePerformance


# menu()
setup()
simulate()
