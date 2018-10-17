from riotwatcher import RiotWatcher

import key

#my api key, XXXXX for privacy
watcher = RiotWatcher(key.APIkey)

#user region
my_region = 'euw1'

summoner_name = raw_input('Enter your summoner name:')

#
try:
    me = watcher.summoner.by_name(my_region,summoner_name)

    print(me)
except:
    print('An error occured!')
