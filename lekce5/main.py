# a = (1, "ano", True, None)
# print(type(a)) #Tuple кортеж 

# print(a[1]) #ano

# a[1] = 'hello' #кортеж нельзя изминить

tuple1 = ("1", "Ano", 12) # распаковка кортежа 
# a, b, c, = tuple1 
# print(a)

# a, b, *rest = tuple1 # 1 Ano [1]
# *start, c = tuple1  # ['1', 'Ano'] 12
# print(start, c)


# list1 = list(tuple1) # изменение кортеже не рокомендовано
# list1[1] = "ne"
# print(type(tuple(list1)), tuple(list1))

# print(tuple1.index(12))
# print(tuple1.count(1))

dict1 = {"a": [1, 2, 1], # dict(Словарь) - обект,
         "b": True,
         "c": 45,
         "d": "Hello"
         }
# print(dict1.get("c", "netu")) # 45
# print(dict1.values()) #dict_values([[1, 2, 1], True, 45, 'Hello'])
# print(dict1.items()) # dict_items([('a', [1, 2, 1]), ('b', True), ('c', 45), ('d', 'Hello')])  розкине по парах
# dict1.update({"isOnline": True})
# print(dict1) {'a': [1, 2, 1], 'b': True, 'c': 45, 'd': 'Hello', 'isOnline': True}

# dict1["d"] = "ahoj" # изменени значение
# print(dict1)

# del dict1["d"] #удаление ключа
# print(dict1)

# new_value = dict1.pop("c")  #{'a': [1, 2, 1], 'b': True, 'd': 'Hello'}
# print(dict1)
# print(new_value) # 45

# for key, value in dict1.items():
#     print(key, value)

# for v in dict1.values():
#     print(v)

# dict()
# # a = dict()
# d = dict([("name", "DEn"), ("age", 33) ])
# print(d)

# d = dict(id=13, login="AlexStep")
# print(d)

# a = ["alex", "Ivan", "Den"]
# b = [33, 44, 2]
# d = dict(zip(a, b)) # zip - обеденает 
# # print(d)

# s = ("1", "f", "c")
# d = dict.fromkeys(s, "Hello")
# print(d)

# fruits = ["Banan", "apple", "orange"]
# fruits_dict = {k: value for k, value in enumerate(fruits)}
# print(fruits_dict) #{0: 'Banan', 1: 'apple', 2: 'orange'}
# fruits_dict = {k: value for k, value in enumerate(fruits) if len(value) > 5}
# print(fruits_dict) #{2: 'orange'}

# set()

# set1 = {1,2, 4, 1,2 ,3, 4, 6}
# print(set1) #{1, 2, 3, 4, 6}
# s = set("hello3")
# print(s)
# print(3 in s) #

# t = {"f", 1}
# print(s|t) 

# frozenset

# s = set("hello3")
# newSer = frozenset(s)
# # print(type(newSer))

# import getpass
# password = getpass.getpass("Enter your password")

# from getpass import getpass
# password = getpass("Enter your password")

# from datetime import datetime as dt
# print(dt.now())


# from turtle import *


# # Настройка черепашки
# color('red')
# fillcolor('yellow')
# shape('turtle')  # Можно использовать 'arrow', 'turtle', 'classic'
# speed(3)

# # Управляющие функции
# def move_forward():
#     forward(200)

# def move_backward():
#     backward(200)

# def turn_left():
#     left(60)

# def turn_right():
#     right(60)

# # Привязка клавиш
# listen()
# onkey(move_forward, 'w')
# onkey(move_backward, 's')
# onkey(turn_right, 'd')
# onkey(turn_left, 'a')

# # Ожидание событий
# done()