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
        api_key = 'RGAPI-6f4cda0c-49d1-42fd-8d47-f6d436d85039'
        api_url = f'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={api_key}'
        w=LolWatcher(api_key)
        summoner = w.summoner.by_name('euw1', summoner_name)
        ranked_stats = w.league.by_summoner('euw1', summoner['id'])

        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()

            # process the data as needed
            return render(request, 'app/player_info.html', {'data': data, 'ranked_stats': ranked_stats})
        else:
            # handle error cases
            return render(request, 'app/tierList.html')
