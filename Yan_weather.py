# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import pickle
import re
# from Places_parser import*

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
    i = 0
    temp_dict = {}
    for rootdir, dirs, files in os.walk(path):
        for file in files:
            with open(f'{path}{file}', 'rb') as file_data:
                target_dict = pickle.load(file_data)
                names = file_data.name.replace(path, '').replace('.data', '')

                if place_name in str(target_dict):
                    i += 1
                    temp_dict[i, names] = target_dict
                    print(f'{i} --- {names}')


    for k, v in temp_dict.items():
        if place_name in str(v):
            for key, value in v.items():
                if key.startswith(place_name):
                    fin_dict[key] = value
                    print(f'{key} ---> {value}')
    #print(fin_dict)

    if i > 1:
        num_of_variant = int(input(f'{i} places with same name. Put number of your varaiant >>> '))
        id = temp_dict[num_of_variant][place_name]
        print(f'Your place id is {id}')

    elif i == 1:
        id = temp_dict[i, place_name]
        print(id)
        return id









if __name__ == '__main__':
    fin_dict = {}
    path = 'D:\\GitHub\\YandexWeather\\pickle_ru\\'
    place = 'Зубово'
    pl = get_places_id(place)
    #get_weather(pl)


