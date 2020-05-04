# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import pickle

place = 'Зубово'
request = requests.get('https://yandex.ru/pogoda/zubovo-republic-of-bashkortostan')
soup = BeautifulSoup(request.text, "html.parser")
temperature = soup.find_all('div', {'class': 'temp fact__temp fact__temp_size_s'})[0].find_all(text=True, recursive=True)
temperature = temperature[1]

wetness = soup.find('div', {'class': 'link__condition day-anchor i-bem'}).get_text()

feel_like_temp = soup.find_all('div', {'class': 'term term_orient_h fact__feels-like'})[0].find_all(text=True, recursive=True)
feel_like_temp = feel_like_temp[1]


def seaching_places_from_txt(place_name):
    url = 'D:\\GitHub\\YandexWeather\\rus\\'
    for rootdir, dirs, files in os.walk(url):
        for file in files:
            with open(url + file, 'r') as txt_file:
                txt = txt_file.read()
                if place_name in txt:
                    print(file)
                    print(txt)







if __name__ == '__main__':

    seaching_places_from_txt('Саитбаба')

    # print(f'Погода в {place}', temperature)
    # print(wetness)
    # print(f'Ощущается как', feel_like_temp)