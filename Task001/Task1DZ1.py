# Урок 1. Ввод-Вывод, операторы ветвления
# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

from random import randint #рандомно задаем трехзначное число
n = randint(100, 1000)
print('Ввод - Трехзначное число:', n)

summa = n//100 + n//10%10 + n%10
print ("Ответ - Сумма цифр трехзначного числа = ", summa)
