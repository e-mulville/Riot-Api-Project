import json

import numpy as np

import API_requests


def main():
    summoner_name = raw_input('Please enter summoner name: ')

    try:
        profile = API_requests.request_profile(summoner_name)

        for key in profile:
            print key, ": ", profile[key]


        matchlist = API_requests.request_match_list(summoner_name)

        newest_match_id = matchlist["matches"][0]["gameId"]

        newest_match = API_requests.request_match(newest_match_id)

        print

        for key in range(0,len(newest_match["participantIdentities"])):
            if newest_match["participantIdentities"][key]["player"]["summonerName"].lower().replace(" ","") == summoner_name.lower().replace(" ",""):
                summoners_participant_Id = newest_match["participantIdentities"][key]["participantId"]

        for key in range(0,len(newest_match["participants"])):
            if newest_match["participants"][key]["participantId"] == summoners_participant_Id:
                print "You got ", newest_match["participants"][key]["stats"]["kills"], " kills in your most recent game."



    except Exception as exc:
        print exc.args[0], exc.args[1]

if __name__ == "__main__":
    main()
