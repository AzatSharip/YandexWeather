# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import os
import pickle
# from YandexWeather.Yan_weather import*


def regions_parser(url):
    time.sleep(sleeping_time)
    countries_dict = dict()
    request = requests.get(url)
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        places = soup.find_all('li', {'class': 'place-list__item'})
        for p in places:
            value = p.find('a').get('href').replace('/pogoda/region/', '').replace('?via=reg', '')
            key = p.find('a').text
            countries_dict[key] = value

        print(f'Elements: {len(countries_dict)}')
        return countries_dict
    else:
        print('Bad request.status_code:', request.status_code)


def cities_parser(country_region, id, path):
    time.sleep(sleeping_time)
    request = requests.get('https://yandex.ru/pogoda/region/'+str(id))
    if request.status_code == 200:
        places_dict = dict()
        countries_dict = dict()
        soup = BeautifulSoup(request.text, "html.parser")
        places = soup.find_all('li', {'class': 'place-list__item'})

        for p in places:
            value = p.find('a').get('href').replace('/pogoda/', '').replace('?via=reg', '')
            key = p.find('a').text
            places_dict[key] = value

        countries_dict[country_region] = places_dict

        os.makedirs(path, exist_ok=True)
        with open(f'{path}{country_region}.data', 'wb') as file:
            pickle.dump(places_dict, file)
            print(f'{country_region} is done!')

    else:
        print('Bad request.status_code on cities_parser module:', request.status_code)

        
def rus_cities(url):
    rus_regions_dict = regions_parser(url)
    rus_lenght = len(rus_regions_dict)
    count = 0
    for region, id in rus_regions_dict.items():
        count += 1
        cities_parser(region, id, path)
        print(f'There are {rus_lenght - count} regions left')
        print('-----------------------------------------')


def world_cities(url):
    countries_dict = regions_parser(url)
    other_lenght = len(countries_dict)
    count = 0
    for country, id in countries_dict.items():
        count += 1
        cities_parser(country, id, path)
        print(f'There are {other_lenght - count} countries left')
        print('-----------------------------------------')




if __name__ == '__main__':
    sleeping_time = 1
    ru_url = 'https://yandex.ru/pogoda/region/225'
    world_url = 'https://yandex.ru/pogoda/region'
    path = 'D:\\GitHub\\YandexWeather\\pickle_ru\\'

    rus_cities(ru_url)
    #world_cities(world_url)












