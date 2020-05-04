# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import pickle
from Places_parser import*

def get_weather(id):
    request = requests.get(f'https://yandex.ru/pogoda/{id}')
    soup = BeautifulSoup(request.text, "html.parser")
    temperature = soup.find_all('div', {'class': 'temp fact__temp fact__temp_size_s'})[0].find_all(text=True, recursive=True)
    temperature = temperature[1]

    wetness = soup.find('div', {'class': 'link__condition day-anchor i-bem'}).get_text()

    feel_like_temp = soup.find_all('div', {'class': 'term term_orient_h fact__feels-like'})[0].find_all(text=True, recursive=True)
    feel_like_temp = feel_like_temp[1]
    print(f'Погода в {place}', temperature)
    print(wetness)
    print(f'Ощущается как', feel_like_temp)



def get_places_id(place_name):
    for rootdir, dirs, files in os.walk(path):
        for file in files:
            with open(f'{path}{file}', 'rb') as file:
                target_dict = pickle.load(file)
                if place_name in target_dict:
                    print(target_dict[place_name])
                    id = target_dict[place_name]
                    return id




if __name__ == '__main__':
    path = 'D:\\GitHub\\YandexWeather\\pickle_ru\\'
    place = 'Оймякон'

    get_weather(get_places_id(place))


