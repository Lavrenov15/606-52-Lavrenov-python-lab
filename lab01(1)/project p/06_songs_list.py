#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут
# Точность указывается в функции round(a, b)
# где a, это число которое надо округлить, а b количество знаков после запятой
# более подробно про функцию round смотрите в документации https://docs.python.org/3/search.html?q=round

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ.XX минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)

# TODO здесь ваш код
# Находим время звучания каждой песни в списке
halo_time = violator_songs_list[3][1]  # 'Halo' на индексе 3
enjoy_time = violator_songs_list[5][1]  # 'Enjoy the Silence' на индексе 5
clean_time = violator_songs_list[8][1]  # 'Clean' на индексе 8

# Вычисляем общее время
total_time_list = halo_time + enjoy_time + clean_time
# Округляем до двух знаков после запятой
total_time_rounded = round(total_time_list, 2)

print(f"Три песни звучат {total_time_rounded} минут")


# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут

# TODO здесь ваш код
# Получаем время звучания из словаря по ключам
sweetest_time = violator_songs_dict['Sweetest Perfection']
policy_time = violator_songs_dict['Policy of Truth']
blue_dress_time = violator_songs_dict['Blue Dress']

# Вычисляем общее время
total_time_dict = sweetest_time + policy_time + blue_dress_time
# Округляем до двух знаков после запятой
total_time_dict_rounded = round(total_time_dict, 2)

print(f"А другие три песни звучат {total_time_dict_rounded} минут")
