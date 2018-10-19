import json

import numpy as np

import API_requests

import keras


def compare_teams(summoners_name):
    try:
        profile = API_requests.request_profile(summoner_name)

    except Exception as exc:
        print exc.args[0], exc.args[1]

    matchlist = API_requests.request_match_list(summoner_name)

    for match_num in range(0,20):
        match_id = matchlist["matches"][0]["gameId"]




def main():
    summoner_name = raw_input('Please enter summoner name: ')

    X = np.zeros((1,101))

    try:
        profile = API_requests.request_profile(summoner_name)

    except Exception as exc:
        print exc.args[0], exc.args[1]

    for key in profile:
        print key, ": ", profile[key]

#requesting matchlist for summoner
    matchlist = API_requests.request_match_list(summoner_name)

#getting their latest match id
    newest_match_id = matchlist["matches"][0]["gameId"]

#requesting the match data
    newest_match = API_requests.request_match(newest_match_id)

    #collecting the participant id for the tartget summoner
    for key in range(0,len(newest_match["participantIdentities"])):
        if newest_match["participantIdentities"][key]["player"]["summonerName"].lower().replace(" ","") == summoner_name.lower().replace(" ",""):
            summoners_participant_Id = newest_match["participantIdentities"][key]["participantId"]

    for key in range(0,len(newest_match["participants"])):
        if newest_match["participants"][key]["participantId"] == summoners_participant_Id:
            print "You got ", newest_match["participants"][key]["stats"]["kills"], " kills in your most recent game."


            #gathering data in a numpy array
            x = 0
            for statskey in newest_match["participants"][key]["stats"]:
                X[0,x] = newest_match["participants"][key]["stats"][statskey]
                x = x + 1



    print X


if __name__ == "__main__":
    main()
