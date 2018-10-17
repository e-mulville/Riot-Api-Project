import json

import requests

import key

def request_profile(name):
    URL = "https://euw1.api.riotgames.com/lol/summoner/v3/summoners/by-name/{}?api_key={}".format(name,key.APIkey)

    profile = requests.get(URL)

    if profile.json().keys()[0] == 'status':
        raise Exception("Error code:", profile.json()['status']['status_code'])

    return profile.json()

def main():
    summoner_name = raw_input('Please enter summoner name: ')

    try:
        profile = request_profile(summoner_name)

        for key in profile:
            print key, ": ", profile[key]
    except Exception as exc:
        print exc.args[0], exc.args[1]

if __name__ == "__main__":
    main()
