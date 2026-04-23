#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
# TODO здесь ваш код
garden_set = set(garden)
meadow_set = set(meadow)
# выведите на консоль все виды цветов
# TODO здесь ваш код
print(garden_set | meadow_set)
# выведите на консоль те, которые растут и там и там
# TODO здесь ваш код
j = 0
flower=[]
while j < len(garden):
    i = 0
    while i < len(meadow):
        if garden[j] == meadow [i]:
            flower.append(garden[j])
            i+=1
        else:
            i+=1
    j+=1
flower = set(flower) 
print("garden + meadow",flower)
# выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код
flower1 = garden_set - meadow_set 
print("only garden",flower1)
# выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код
flower2 = meadow_set - garden_set
print("only meadow",flower2)