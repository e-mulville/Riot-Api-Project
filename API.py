from riotwatcher import RiotWatcher


#my api key, XXXXX for privacy
watcher = RiotWatcher('RGAPI-9e97549d-1ab3-4f7a-8f45-010e2d3760e2')

#user region
my_region = 'euw1'

summoner_name = raw_input('Enter your summoner name:')

#
try:
    me = watcher.summoner.by_name(my_region,summoner_name)

    print(me)
except:
    print('An error occured!')
