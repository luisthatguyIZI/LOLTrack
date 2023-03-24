from django.shortcuts import render
import requests
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

def player_info_view(request):
    api_key = 'RGAPI-7369fa4b-0afe-49a3-9307-04aaca793da9'
    region = 'EUW1'
    puuid = 'VVbkrzvOCMvMk_eGgl5Rv3bUrLSNT0iiBbwXSKWBauv3QY8u2MtfJKXienRSM0XzM1H8J_ACdlgANg'

    api_url = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/Ab0minati0n15"

    api_url = api_url + '?api_key=' + api_key
    match_api_url='https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/VVbkrzvOCMvMk_eGgl5Rv3bUrLSNT0iiBbwXSKWBauv3QY8u2MtfJKXienRSM0XzM1H8J_ACdlgANg/ids?start=0&count=20'
    match_api_url= match_api_url + "&api_key=" + api_key

    resp = requests.get(api_url)
    match_resp = requests.get(match_api_url)

    match_list = match_resp.json()
    player_info = resp.json()



    return render(request, 'app/player_info.html', {'player_info': player_info, 'match_info': match_list})

