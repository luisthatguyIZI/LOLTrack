from django.shortcuts import render
import requests
from riotwatcher import LolWatcher
from django.http import HttpResponse


def base(response):
    return render(response, "app/base.html", {})


def home(response):
    return render(response, "app/home.html", {})

def profile(response):
    return render(response, "app/profile.html", {})

def champions(response):
    return render(response, "app/champions.html", {})

def tierlist(response):
    return render(response, "app/tierList.html", {})

def live(response):
    return render(response, "app/live.html", {})



def player_view(request):
    if request.method == 'GET':
        summoner_name = request.GET.get('summoner_name')
        api_key = 'RGAPI-0f7e7412-c47e-4167-988f-a4183651fd5e'
        w = LolWatcher(api_key)

        # Get summoner information
        summoner = w.summoner.by_name('euw1', summoner_name)
        puuid = summoner['puuid']

        # Get ranked stats
        ranked_stats = w.league.by_summoner('euw1', summoner['id'])

        # Get match history
        match_history = w.match.matchlist_by_puuid('EUROPE', puuid)

        match_info=[]
        for i in range(len(match_history)):
            matchID=match_history[i]
            matchData_api_url = 'https://europe.api.riotgames.com/lol/match/v5/matches/' + matchID
            matchData_api_url = matchData_api_url + "?api_key=" + api_key
            matchData_resp = (requests.get(matchData_api_url))
            match_data = (matchData_resp.json())
            me = (match_data['metadata']['participants'].index(puuid))
            champ=(match_data['info']['participants'][me]['championName'])
            outcome=(match_data['info']['participants'][me]['win'])
            kills=(match_data['info']['participants'][me]['kills'])
            assists=(match_data['info']['participants'][me]['assists'])
            deaths=(match_data['info']['participants'][me]['deaths'])
            role=(match_data['info']['participants'][me]['role'])
            totdamg=(match_data['info']['participants'][me]['totalDamageDealt'])
            kda=(kills+assists)/deaths
            match_info.append({'outcome': outcome, 'champ': champ, 'kills': kills, 'assists': assists, 'deaths': deaths, 'role': role, 'totdamg': totdamg, 'kda': kda})
            return render(request, 'app/player_info.html',{'summoner': summoner, 'ranked_stats': ranked_stats, 'match_history': match_history,'match_info': match_info})

##COULD USE 1 ARRAY TO STORE THE MATCH_INFO[0],MATCH_INFO[1]....