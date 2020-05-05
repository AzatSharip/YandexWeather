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
    id_list = []
    for rootdir, dirs, files in os.walk(path):
        for file in files:
            with open(f'{path}{file}', 'rb') as file_data:
                target_dict = pickle.load(file_data)
                names = file_data.name.replace(path, '').replace('.data', '')
                for key, value in target_dict.items():
                    if key.startswith(place_name):
                        i += 1
                        id_list.append(value)
                        print(f'{i} ---> {key} ({names})')
    #print(id_list)
    print('-----------------------------------')
    if len(id_list) > 1:
        num_of_variant = int(input(f'We found {i} places with similar names. Enter the number of your region from the list >>> '))
        print('-----------------------------------')
        id = id_list[num_of_variant-1]
        return id
    elif len(id_list) == 1:
        id = id_list[0]
        return id
    elif len(id_list) < 1:
        print('There\'s no such place!')



if __name__ == '__main__':
    place = input('Enter the name of the locality you want to know the weather for >>> ')
    fin_dict = {}
    #path = 'D:\\GitHub\\YandexWeather\\pickle_world\\'
    path = 'D:\\GitHub\\YandexWeather\\pickle_ru\\'

    pl = get_places_id(place)
    get_weather(pl)


