#Подсчитать, сколько было выделено памяти под переменные в ранее
# разработанных программах в рамках первых трех уроков. Проанализировать
# результат и определить программы с наиболее эффективным использованием памяти.

#Версия Python: python Python 3.9.6
#Windows 10 x64

import sys


def show_size(x, level=0):

    size_par = sys.getsizeof(x)
    print('\t' * level, f'type={type(x)}, size={size_par}, object={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                size_par = size_par + sys.getsizeof(key)
                show_size(value, level + 1)
                size_par = size_par + sys.getsizeof(value)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)
                size_par = size_par + sys.getsizeof(item)
    return size_par

#оценим программу с 1 урока. Найти сумму и произведение цифр трехзначного
# числа, которое вводит пользователь.

a = input('Введите трехзначное число: ')

x = int(a[0])
y = int(a[1])
z = int(a[2])

sum_l = x + y + z
mult = x * y * z

sum_member = sys.getsizeof(a) + sys.getsizeof(x) + sys.getsizeof(y) + sys.getsizeof(z) + sys.getsizeof(
    sum_l) + sys.getsizeof(mult)
print('В программе задействовано байт памяти: {}'.format(sum_member))

#В программе задействовано байт памяти: 192

#оценим программу с 2 урока. Сформировать из введенного числа обратное по порядку
# входящих в него цифр и вывести на экран. Например, если введено число 3486,
# то надо вывести число 6843.

new_num = ''
# show_size(new_num)

num = input('Введите число: ')
count = len(num)
k = range(count)

for i in k:
    new_num = new_num + str(int(num) % 10)
    # show_size(new_num)
    num = int(num) // 10
    # show_size(num)
print(new_num)

sum_member2 = show_size(new_num) + show_size(num) + show_size(count) + show_size(k)
print('В программе задействовано байт памяти: {}'.format(sum_member2))

#результаты:
#type=<class 'str'>, size=52, object=321
# type=<class 'int'>, size=24, object=0
# type=<class 'int'>, size=28, object=3
# type=<class 'range'>, size=48, object=range(0, 3)
# type=<class 'int'>, size=24, object=0
# type=<class 'int'>, size=28, object=1
# type=<class 'int'>, size=28, object=2
# В программе задействовано байт памяти: 232

#оценим программу с 2 урока. Во втором массиве сохранить индексы четных элементов первого
# массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во
# второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 – если
# индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

import random

g = range(9)

mas_num = [random.randint(1, 100) for n in g]
print('Дан массив элементов: {}'.format(mas_num))

mas_index = [mas_num.index(i) for i in mas_num if i % 2 == 0]
print('Массив индексов четных элементов: {}'.format(mas_index))

sum_member3 = show_size(mas_num) + show_size(num) + show_size(g)
print('В программе задействовано байт памяти: {}'.format(sum_member3))

#Дан массив элементов: [31, 55, 10, 95, 70, 43, 21, 30, 57]
# Массив индексов четных элементов: [2, 4, 7]
# type=<class 'list'>, size=184, object=[31, 55, 10, 95, 70, 43, 21, 30, 57]
# type=<class 'int'>, size=28, object=31
# type=<class 'int'>, size=28, object=55
# type=<class 'int'>, size=28, object=10
# type=<class 'int'>, size=28, object=95
# type=<class 'int'>, size=28, object=70
# type=<class 'int'>, size=28, object=43
# type=<class 'int'>, size=28, object=21
# type=<class 'int'>, size=28, object=30
# type=<class 'int'>, size=28, object=57
# type=<class 'int'>, size=24, object=0
# type=<class 'range'>, size=48, object=range(0, 9)
# type=<class 'int'>, size=24, object=0
# type=<class 'int'>, size=28, object=1
# type=<class 'int'>, size=28, object=2
# type=<class 'int'>, size=28, object=3
# type=<class 'int'>, size=28, object=4
# type=<class 'int'>, size=28, object=5
# type=<class 'int'>, size=28, object=6
# type=<class 'int'>, size=28, object=7
# type=<class 'int'>, size=28, object=8
# В программе задействовано байт памяти: 756



