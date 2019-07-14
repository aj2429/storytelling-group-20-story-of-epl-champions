import csv

TeamCurrMatchPlayed = {}
TeamData = {}

with open("data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0

    for row in csv_reader:
        if (line_count == 0):
            line_count+=1;
            continue;

        line_count+=1;

        HomeTeam = row[2]
        AwayTeam = row[3]
        WinningTeam = row[6]
        HomeTeamGoals = int(row[4])
        AwayTeamGoals = int(row[5])
        HomeTeamGD = HomeTeamGoals - AwayTeamGoals
        AwayTeamGD = AwayTeamGoals - HomeTeamGoals

        #print("Home Team: %s HomeTeamGD : %d") % (HomeTeam, HomeTeamGD)

        HomeTeamPoints = 0

        AwayTeamPoints = 0
        if (WinningTeam == 'H'):
            HomeTeamPoints = 3
        elif (WinningTeam == 'A'):
            AwayTeamPoints = 3
        else:
            HomeTeamPoints = 1
            AwayTeamPoints = 1

        #print(HomeTeamPoints)

        if HomeTeam not in TeamData:
            TeamData[HomeTeam] = {1 : {"GD" : HomeTeamGD, "Points" : HomeTeamPoints}}
            TeamCurrMatchPlayed[HomeTeam] = 1
        else:
            TeamData[HomeTeam].update({TeamCurrMatchPlayed[HomeTeam]+1 : {"GD" : TeamData[HomeTeam][TeamCurrMatchPlayed[HomeTeam]]["GD"] + HomeTeamGD, "Points" : TeamData[HomeTeam][TeamCurrMatchPlayed[HomeTeam]]["Points"] + HomeTeamPoints}})
            TeamCurrMatchPlayed[HomeTeam] += 1

        if AwayTeam not in TeamData:
            TeamData[AwayTeam] = {1 : {"GD" : AwayTeamGD, "Points" : AwayTeamPoints}}
            TeamCurrMatchPlayed[AwayTeam] = 1
        else:
            TeamData[AwayTeam].update({TeamCurrMatchPlayed[AwayTeam]+1 : {"GD" : TeamData[AwayTeam][TeamCurrMatchPlayed[AwayTeam]]["GD"] + AwayTeamGD, "Points" : TeamData[AwayTeam][TeamCurrMatchPlayed[AwayTeam]]["Points"] + AwayTeamPoints}})
            TeamCurrMatchPlayed[AwayTeam] += 1

#print(TeamData)


with open('transformed_2015_2016.csv', mode='w') as dataFile:
    df_writer = csv.writer(dataFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for key in TeamData:
        #print(key)

        for subKey in TeamData[key]:
            #print(subKey)
            #print(TeamData[key][subKey]["Points"])
            #print(TeamData[key][subKey]["GD"])
            #print(key, subKey, TeamData[key][subKey]["Points"], TeamData[key][subKey]["GD"])
            df_writer.writerow([key, subKey, TeamData[key][subKey]["Points"], TeamData[key][subKey]["GD"]])
