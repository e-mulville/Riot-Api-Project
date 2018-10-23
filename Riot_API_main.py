import json
import time
import numpy as np

import API_requests

import keras

def print_scores(array):
    print "K/D/A: {}/{}/{}  CS: {} Damage to champions: {}".format(array[0],array[1],array[2],array[3],array[4])





#kills/deaths/assists/cs/damagedealt to champions
def average_score(summoner_id):
    #how many games to average over
    num_of_games = 5
    ####
    Scores_array = np.zeros((num_of_games, 5))

    matchlist = API_requests.request_match_list(summoner_id)

    try:
        profile = API_requests.request_profile_id(summoner_id)

    except Exception as exc:
        print exc.args[0], exc.args[1]

    summoner_name = profile["name"]


    #for the last 10 games
    for match_num in range(0,num_of_games):

        match_id = matchlist["matches"][match_num]["gameId"]

        match = API_requests.request_match(match_id)

        for key in range(0,len(match["participantIdentities"])):
            #make not of the targets participant Id
            if match["participantIdentities"][key]["player"]["summonerName"].lower().replace(" ","") == summoner_name.lower().replace(" ",""):
                summoners_participant_Id = match["participantIdentities"][key]["participantId"]

        for key in range(0,len(match["participants"])):
            #if the stats match the participant Id put their stats in the array
            if match["participants"][key]["participantId"] == summoners_participant_Id:
                Scores_array[match_num, 0] = match["participants"][key]["stats"]["kills"]
                Scores_array[match_num, 1] = match["participants"][key]["stats"]["deaths"]
                Scores_array[match_num, 2] = match["participants"][key]["stats"]["assists"]
                Scores_array[match_num, 3] = match["participants"][key]["stats"]["totalMinionsKilled"]
                Scores_array[match_num, 4] = match["participants"][key]["stats"]["totalDamageDealtToChampions"]

    #return the average accross all 10 games
    return np.mean(Scores_array, axis = 0)



def compare_teams(summoner_name):

    #how many games to look at for the target summoner
    matches_of_summoner = 5
    ####

    team_scores_array = np.zeros((0,5))
    oppenent_scores_array = np.zeros((0,5))

    try:
        profile = API_requests.request_profile_name(summoner_name)

    except Exception as exc:
        print exc.args[0], exc.args[1]



    summoner_id = profile["accountId"]

    matchlist = API_requests.request_match_list(summoner_id)

    for match_num in range(0,matches_of_summoner):
        print "Looking at match:", match_num

        match_id = matchlist["matches"][match_num]["gameId"]

        match = API_requests.request_match(match_id)

        #go through the dictionary to find out the participant_id and team_id of the target summoner
        for key in range(0,len(match["participantIdentities"])):
            if match["participantIdentities"][key]["player"]["summonerName"].lower().replace(" ","") == summoner_name.lower().replace(" ",""):
                summoner_participant_id = match["participantIdentities"][key]["participantId"]
                #finding targets team id
                for stats_key in range(0,len(match["participants"])):
                    if match["participants"][key]["participantId"] == summoner_participant_id:
                        summoner_teamid = match["participants"][key]["teamId"]

        for key in range(0,len(match["participantIdentities"])):
        #go through all of the others last X games and aveage their score.
                player_id = match["participantIdentities"][key]["participantId"]

                if player_id != summoner_participant_id:

                    for stats_key in range(0,len(match["participants"])):
                        #get the right player's stats and check what team they are on
                        if match["participants"][stats_key]["participantId"] == player_id:
                            if match["participants"][stats_key]["teamId"] == summoner_teamid:
                                X = average_score(match["participantIdentities"][stats_key]["player"]["accountId"])
                                X1 = np.expand_dims(X,axis = 0)
                                team_scores_array = np.concatenate((team_scores_array, X1))
                            else:
                                X = average_score(match["participantIdentities"][stats_key]["player"]["accountId"])
                                X1 = np.expand_dims(X,axis = 0)
                                oppenent_scores_array = np.concatenate((oppenent_scores_array, X1))

    print "Your average teammate is:"
    print_scores(np.mean(team_scores_array, axis = 0))

    print "Your average oppponent is: "
    print_scores(np.mean(oppenent_scores_array, axis = 0))


def main():
    summoner_name = raw_input('Please enter summoner name: ')

    compare_teams(summoner_name)


#saftey
if __name__ == "__main__":
    main()
