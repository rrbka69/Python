# Задача №35.
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

def simple(n,del1 = 2):
    if n == 2 or del1*del1 > n:
        return print ('{} - простое число'.format(n))
    elif n % del1 == 0:
        return print('{} - составное число'.format(n))
    return simple(n, del1 + 1)
simple (6)
   
            