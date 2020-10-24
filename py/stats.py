import pandas as pd

drivers = pd.read_csv("..\data\drivers.csv", usecols=["driverId", "driverRef", "number", "code", "forename", "surname"])
circuits = pd.read_csv("..\data\circuits.csv", usecols=["circuitId", "circuitRef", "name", "location", "country"])
races = pd.read_csv("..\data\\races.csv", usecols=["raceId", "year", "round", "circuitId", "name"])
results = pd.read_csv("..\data\\results.csv", usecols=["resultId", "raceId", "driverId", "constructorId", "number", "grid", "position"])
constructors = pd.read_csv("..\data\constructors.csv", usecols=["constructorId", "constructorRef", "name"])
qualifying = pd.read_csv("..\data\qualifying.csv", usecols=["qualifyId", "driverId", "constructorId", "position"])

# print(drivers)
# print(drivers["driverId"])
def findAverage():
    averagePositions = {}
    for i in range(drivers["driverId"].shape[0]):
        # averageFinish = 0
        sumPositions = 0
        numRaces = 0
        driverId = drivers.at[i, "driverId"]
        for j in range(results["resultId"].shape[0]):
            if driverId == results.at[j, "driverId"]:
                numRaces = numRaces + 1
                try:
                    pos = int(results.at[j, "position"])
                    sumPositions += pos
                except ValueError:
                    continue
        try:
            averagePositions[driverId] = int(round(sumPositions / numRaces))
        except ZeroDivisionError:
            averagePositions[driverId] = 21

    return averagePositions


def findAverageQuali():
    averageQuali = {}
    for i in range(drivers["driverId"].shape[0]):
        # averageFinish = 0
        sumPositions = 0
        numRaces = 0
        driverId = drivers.at[i, "driverId"]
        for j in range(qualifying["qualifyId"].shape[0]):
            if driverId == qualifying.at[j, "driverId"]:
                numRaces = numRaces + 1
                try:
                    pos = int(qualifying.at[j, "position"])
                    sumPositions += pos
                except ValueError:
                    continue

        try:
            averageQuali[driverId] = int(round(sumPositions / numRaces))
        except ZeroDivisionError:
            averageQuali[driverId] = 21

    return averageQuali

def findAverageConstructorQuali():
    averageQuali = {}
    for i in range(constructors["constructorId"].shape[0]):
        # averageFinish = 0
        sumPositions = 0
        numRaces = 0
        constructorId = constructors.at[i, "constructorId"]
        for j in range(qualifying["qualifyId"].shape[0]):
            if constructorId == qualifying.at[j, "constructorId"]:
                numRaces = numRaces + 1
                try:
                    pos = int(qualifying.at[j, "position"])
                    sumPositions += pos
                except ValueError:
                    continue

        try:
            averageQuali[constructorId] = int(round(sumPositions / numRaces))
        except ZeroDivisionError:
            averageQuali[constructorId] = 21

    return averageQuali

def findAverageConstructor():
    averagePositions = {}
    for i in range(constructors["constructorId"].shape[0]):

        sumPositions = 0
        numRaces = 0
        constructorId = constructors.at[i, "constructorId"]
        for j in range(results["resultId"].shape[0]):
            if constructorId == results.at[j, "constructorId"]:
                numRaces = numRaces + 1
                try:
                    pos = int(results.at[j, "position"])
                    sumPositions += pos
                except ValueError:
                    continue

        try:
            averagePositions[constructorId] = int(round(sumPositions / numRaces))
        except ZeroDivisionError:
            averagePositions[constructorId] = 21

    return averagePositions

#to find quali stats
print('driverId,averageQuali')
dict_data = findAverageQuali()

#to find race stats
#print('driverId,averageFinish')
#dict_data = findAverage()

#to find constructor quali stats
#print('constructorId,averageQuali')
#dict_data = findAverageConstructorQuali()

#to find constructor race stats
#print('constructorId,averageFinish')
#dict_data = findAverageConstructor()

for k, v in dict_data.items():
    print(k, v)

