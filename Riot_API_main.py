import json
import time
import numpy as np

import API_requests

import keras


#kills/deaths/assists/cs/damagedealt to champions
def average_score(summoner_name):
    Scores_array = np.zeros((10, 5))

    try:
        profile = API_requests.request_profile(summoner_name)

    except Exception as exc:
        print exc.args[0], exc.args[1]

    matchlist = API_requests.request_match_list(summoner_name)

    for match_num in range(0,10):

        time.sleep(1)

        match_id = matchlist["matches"][match_num]["gameId"]

        match = API_requests.request_match(match_id)

        for key in range(0,len(match["participantIdentities"])):
            #make not of the targets participant Id
            if match["participantIdentities"][key]["player"]["summonerName"].lower().replace(" ","") == summoner_name.lower().replace(" ",""):
                summoners_participant_Id = match["participantIdentities"][key]["participantId"]

        for key in range(0,len(match["participants"])):
            if match["participants"][key]["participantId"] == summoners_participant_Id:
                Scores_array[match_num, 0] = match["participants"][key]["stats"]["kills"]
                Scores_array[match_num, 1] = match["participants"][key]["stats"]["deaths"]
                Scores_array[match_num, 2] = match["participants"][key]["stats"]["assists"]
                Scores_array[match_num, 3] = match["participants"][key]["stats"]["totalMinionsKilled"]
                Scores_array[match_num, 4] = match["participants"][key]["stats"]["totalDamageDealtToChampions"]

    print Scores_array



def compare_teams(summoner_name):
    try:
        profile = API_requests.request_profile(summoner_name)

    except Exception as exc:
        print exc.args[0], exc.args[1]

    matchlist = API_requests.request_match_list(summoner_name)

    for match_num in range(0,20):
        match_id = matchlist["matches"][match_num]["gameId"]

        match = API_requests.request_match(newest_match_id)

        for key in range(0,len(newest_match["participantIdentities"])):
            #make note of the targets participant Id
            if newest_match["participantIdentities"][key]["player"]["summonerName"].lower().replace(" ","") == summoner_name.lower().replace(" ",""):
                summoners_participant_Id = newest_match["participantIdentities"][key]["participantId"]
            #go through all of the others last 10 games and aveage their score.
            else:
                try:
                    profile = API_requests.request_profile(summoner_name)

                except Exception as exc:
                    print exc.args[0], exc.args[1]

                matchlist = API_requests.request_match_list(summoner_name)

                for match_num in range(0,20):
                    match_id = matchlist["matches"][match_num]["gameId"]

                    match = API_requests.request_match(newest_match_id)


def main():
    summoner_name = raw_input('Please enter summoner name: ')

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


    average_score(summoner_name)



if __name__ == "__main__":
    main()
