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

print('Введите последовательно три целых числа')
first = input('Введите  первое число : ')
if first.isdigit() :
    first = int(first)
else:
    first = 0
second = input('Введите  второе число : ')
if second.isdigit() :
    second = int(first)
else:
    second = 0

# print(first.isdigit())
#first = int(first)
print(type(first))
#if type(first) not <class int>
#second
#third


