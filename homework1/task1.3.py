# Задача 2: Найдите сумму цифр трехзначного числа. 
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n = int(input('Введите целое трехзначное число:'))
n = int(n)
sum = (n//100)+((n//10)%10)+(n%10)
print('Сумма трехзначного числа:', sum)