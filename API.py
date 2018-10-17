import json

import requests

import key

def request_profile(name):
    URL = "https://euw1.api.riotgames.com/lol/summoner/v3/summoners/by-name/{}?api_key={}".format(name,key.APIkey)
    profile = requests.get(URL)
    return profile.json()

def main():
    summoner_name = raw_input('Please enter summoner name: ')

    profile = request_profile(summoner_name)

    for key in profile:
        print key, ": ", profile[key]

if __name__ == "__main__":
    main()
