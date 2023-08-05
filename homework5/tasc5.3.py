# Задача №35.
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

a = 1

def f(a):
    if a == 0:
        return (a/a)
    else:
        return a %1 == 0
    
a = a+1
if (a<=0):
    print ('yes')
else:
    print ('no')


def prime(number):
    n = number
    counter = 0
    for i in range(1, n + 1):
        if n % i == 0:
            counter += 1
    return 'Простое число' if counter == 2 else 'Составное число'


