#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
x1,y1 = sites['Moscow']
x2,y2 = sites['London']
x3,y3 = sites['Paris']

distances = {
    'Moscow':{'London': ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 , 'Paris': ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5},
    'London':{'Moscow': ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 , 'Paris': ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5},
    'Paris':{'Moscow': ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5, 'London': ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5}
}

# TODO здесь заполнение словаря

print(distances)




