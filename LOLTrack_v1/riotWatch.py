from riotwatcher import LolWatcher, ApiError

lol_watcher = LolWatcher('RGAPI-08e8c6e4-6550-4800-af74-1ffdc91e82f4')

my_region = 'EUW1'

me = lol_watcher.summoner.by_name(my_region, 'Ab0minati0n15')
print(me)

# all objects are returned (by default) as a dict
# lets see if i got diamond yet (i probably didnt)
my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])
print(my_ranked_stats)
