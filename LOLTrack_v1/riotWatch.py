from riotwatcher import LolWatcher
import requests

api_key = 'RGAPI-7369fa4b-0afe-49a3-9307-04aaca793da9'
region = 'EUW1'
puuid = 'VVbkrzvOCMvMk_eGgl5Rv3bUrLSNT0iiBbwXSKWBauv3QY8u2MtfJKXienRSM0XzM1H8J_ACdlgANg'
username=""
match_id=""

api_url = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/Ab0minati0n15"

api_url = api_url + '?api_key=' + api_key
matchList_api_url='https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/VVbkrzvOCMvMk_eGgl5Rv3bUrLSNT0iiBbwXSKWBauv3QY8u2MtfJKXienRSM0XzM1H8J_ACdlgANg/ids?start=0&count=20'
matchList_api_url= matchList_api_url + "&api_key=" + api_key
matchData_api_url='https://europe.api.riotgames.com/lol/match/v5/matches/EUW1_6285464160'
matchData_api_url= matchData_api_url + "?api_key=" + api_key

resp = (requests.get(api_url))
matchList_resp=(requests.get(matchList_api_url))
matchData_resp=(requests.get(matchData_api_url))

match_list=(matchList_resp.json())
match_data=(matchData_resp.json())
player_info=(resp.json())

me=(match_data['metadata']['participants'].index(puuid))
#print(match_data['info']['participants'][me]['championName'])

kda=((match_data['info']['participants'][me]['kills']) + (match_data['info']['participants'][me]['assists'])) / (match_data['info']['participants'][me]['deaths'])
#print(kda)


summoner_name='Ab0minati0n15'
w = LolWatcher(api_key)
summoner = w.summoner.by_name('euw1', summoner_name)
ranked_stats = w.league.by_summoner('euw1', summoner['id'])




#print(match_api_url)
#print(api_url)
player_id=(player_info["puuid"])
print(player_id)

