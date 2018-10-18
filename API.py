import json

import requests

import key

#function to return the dictionary of the players profile
def request_profile(name):
    URL = "https://euw1.api.riotgames.com/lol/summoner/v3/summoners/by-name/{}?api_key={}".format(name,key.APIkey)

    profile = requests.get(URL)

    if profile.json().keys()[0] == 'status':
        raise Exception("Error code:", profile.json()['status']['status_code'])

    return profile.json()

#function to return the dictionary of the players match list
def request_match_list(name):
    requested_profile = request_profile(name)

    accountid = requested_profile['accountId']

    URL = "https://euw1.api.riotgames.com/lol/match/v3/matchlists/by-account/{}?api_key={}".format(accountid,key.APIkey)

    match_list = requests.get(URL)

    if match_list.json().keys()[0] == 'status':
        raise Exception("Error code:", match_list.json()['status']['status_code'])

    return match_list.json()

def request_match(match_id):

    URL = "https://euw1.api.riotgames.com/lol/match/v3/matches/{}?api_key={}".format(match_id,key.APIkey)

    match = requests.get(URL)

    if match.json().keys()[0] == 'status':
        raise Exception("Error code:", match.json()['status']['status_code'])

    return match.json()

def main():
    summoner_name = raw_input('Please enter summoner name: ')

    try:
        profile = request_profile(summoner_name)

        for key in profile:
            print key, ": ", profile[key]


        matchlist = request_match_list(summoner_name)

        newest_match_id = matchlist["matches"][0]["gameId"]

        newest_match = request_match(newest_match_id)

        print

        for key in range(0,len(newest_match["participantIdentities"])):
            if newest_match["participantIdentities"][key]["player"]["summonerName"].lower() == summoner_name.lower():
                print newest_match["participantIdentities"][key]["participantId"]


    except Exception as exc:
        print exc.args[0], exc.args[1]

if __name__ == "__main__":
    main()
