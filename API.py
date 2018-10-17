from riotwatcher import RiotWatcher

watcher = RiotWatcher('XXXXXXXXXXXXXXXXXX')
my_region = 'euw1'

me = watcher.summoner.by_name(my_region,'chaos effect')

print(me)
