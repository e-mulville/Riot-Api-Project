import json

import numpy as np

import API_requests
import Compare_teams


import keras


def save_match_data(summoner_name):

    file = open("match_data_array.npy", "w")

    team_100_stats = np.zeros((4,4))

    try:
        profile = API_requests.request_profile_name(summoner_name)

    except Exception as exc:
        print exc.args[0], exc.args[1]

    temp = 0

    summoner_id = profile["accountId"]

    matchlist = API_requests.request_match_list(summoner_id)

    for match_num in matchlist["matches"]:
        match = API_requests.request_match(match_num["gameId"])

        #all match data on a player printed

        print match["participants"][0]["spell1Id"]
        print match["participants"][0]["spell2Id"]
        print match["participants"][0]["highestAchievedSeasonTier"]
        print match["participants"][0]["teamId"]
        print match["participants"][0]["championId"]
        print match["participants"][0]["participantId"]
        for key in match["participants"][0]["stats"]:
            print match["participants"][0]["stats"][key]
        for key in match["participants"][0]["timeline"]:
            if isinstance(match["participants"][0]["timeline"][key], dict):
                for deltaskey in match["participants"][0]["timeline"][key]:
                    print match["participants"][0]["timeline"][key][deltaskey]
            else:
                 match["participants"][0]["timeline"][key]



    np.save(file, test_array)






    file.close()
    file = open("match_data_array.npy", "r")
    output_array = np.load(file)
    file.close()
    print output_array


def main():
    save_match_data("chaoseffect")

    #summoner_name = raw_input('Please enter summoner name: ')
    #Compare_teams.compare_teams(summoner_name)


#saftey
if __name__ == "__main__":
    main()
