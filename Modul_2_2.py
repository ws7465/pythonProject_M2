# Задача "Все ли равны?":
# На вход программе подаются 3 целых числа и записываются
#   в переменные first, second и third соответственно.
# Ваша задача написать условную конструкцию (из if, elif, else),
#   которая выводит кол-во одинаковых чисел среди 3-х введённых.
#
#    Пункты задачи:
#   1.	Если все числа равны между собой, то вывести 3
#   2.	Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
#   3.	Если равных чисел среди 3-х вообще нет, то вывести 0
#
print('Введите последовательно три целых числа')
first = input('Введите  первое число : ')
# контроль ввода именно числа
if first.isdigit() :
    first = int(first)
else:
    first = 0
second = input('Введите  второе число : ')
# контроль ввода именно числа
if second.isdigit() :
    second = int(second)
else:
    second = 0
third = input('Введите  третье число : ')
# контроль ввода именно числа
if third.isdigit() :
    third = int(third)
else:
    third = 0
# если все три равны между собой и не равны 0
if first == second == third != 0 :
    print(3)
# если равны попарно и не равны третьему
elif  0 != first == second != third or 0 != third == first != second or 0 != second == third != first :
    print(2)
# если все разные или не числа
else :
    print(0)
#
# конец задачи

# print(first.isdigit())
#first = int(first)
#print(type(first))
#if type(first) not <class int>
#second
#third


