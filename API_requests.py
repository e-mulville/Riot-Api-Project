import requests
import time
import key

#function to return the dictionary of the players profile from their username
def request_profile_name(name):
    time.sleep(1)
    URL = u"https://euw1.api.riotgames.com/lol/summoner/v3/summoners/by-name/{}?api_key={}".format(name,key.APIkey)
    profile = requests.get(URL)

    if profile.json().keys()[0] == 'status':
        raise Exception("Error code:", profile.json()['status']['status_code'], name)

    return profile.json()

#function to return the dictionary of the players profile
def request_profile_id(account_id):
    time.sleep(1)
    URL = u"https://euw1.api.riotgames.com/lol/summoner/v3/summoners/by-account/{}?api_key={}".format(account_id,key.APIkey)

    profile = requests.get(URL)

    if profile.json().keys()[0] == 'status':
        raise Exception("Error code:", profile.json()['status']['status_code'], account_id)

    return profile.json()

#function to return the dictionary of the players match list
def request_match_list(account_id):
    time.sleep(1)

    URL = u"https://euw1.api.riotgames.com/lol/match/v3/matchlists/by-account/{}?api_key={}".format(account_id,key.APIkey)

    match_list = requests.get(URL)

    if match_list.json().keys()[0] == 'status':
        raise Exception("Error code:", match_list.json()['status']['status_code'], account_id)

    return match_list.json()

#returns match data from the match id
def request_match(match_id):
    time.sleep(1)
    URL = u"https://euw1.api.riotgames.com/lol/match/v3/matches/{}?api_key={}".format(match_id,key.APIkey)

    match = requests.get(URL)

    if match.json().keys()[0] == 'status':
        raise Exception("Error code:", match.json()['status']['status_code'], match_id)

    return match.json()
