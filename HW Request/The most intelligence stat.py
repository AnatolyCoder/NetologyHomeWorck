import requests
import json


r = requests.get('https://akabab.github.io/superhero-api/api/all.json')

list_heroes = json.loads(r.text)

for hero_dict in list_heroes:
    for key, value in hero_dict.items():
        if value == 'Hulk':
            hulk_intelligence = hero_dict["powerstats"]["intelligence"]
        if value == 'Captain America':
            captain_america_intelligence = hero_dict["powerstats"]["intelligence"]
        if value == 'Thanos':
            thanos_intelligence = hero_dict["powerstats"]["intelligence"]
print(f'Hulk: {hulk_intelligence}\nCaptain America: {captain_america_intelligence}\nThanos: {thanos_intelligence}\n')

if hulk_intelligence > captain_america_intelligence and hulk_intelligence > thanos_intelligence:
    print(f'Hulk has the most intelligence stat: {hulk_intelligence}')
elif captain_america_intelligence > hulk_intelligence > thanos_intelligence:
    print(f'Captain America has the most intelligence stat: {captain_america_intelligence}')
else: print(f'Thanos has the most intelligence stat: {thanos_intelligence}')


