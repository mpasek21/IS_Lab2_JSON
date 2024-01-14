# -*- coding: utf-8 -*-
"""
deserialize json
"""
import json
wojewodztwa = ["dolnośląskie", "kujawsko-pomorskie", "lubelskie", "lubuskie", "łódzkie", "malopolskie", "mazowieckie", "opolskie",
               "podkarpackie", "podlaskie", "pomorskie", "śląskie", "świętokrzyskie", "warmińsko-mazurskie", "wielkopolskie", "zachodniopomorskie"]
typ = ["GW", "GMW", "P"]
class DeserializeJson:
# konstruktor
    def __init__(self, filename):
        print("let's deserialize something")
        tempdata = open(filename, encoding="utf8")
        self.data = json.load(tempdata)
# przykładowe statystyki

    def somestats(self):

        for woj in wojewodztwa:
            example_stat = 0
            for t in typ:
                for dep in self.data:
                    if dep['typ_JST'] == t and dep['Województwo'] == woj:
                        example_stat += 1
                print('liczba urzędów ' + t + ' w województwie: ' + woj + ' ' + str(example_stat))