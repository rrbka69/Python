# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть
# 5 -> 1 0 1 1 0
# 2

n = int(input('Введите количество монеток n: '))
n1 = 0  # n1 = gerb 
n2 = 0  # n2 = rehka
count = 0
while count < n:
    count += 1
    m = int(input(f"Введите положение монетки {count} (1 - орел, 0 - решка): "))
    if m:
        n1 += 1
    else:
        n2 += 1
if n1 > n2:
    print(f'Надо перевернуть {n2} монет')
else:
    print(f'Надо перевернуть {n1} монет')