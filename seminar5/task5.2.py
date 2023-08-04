# найти факториал, рекурсия

def fact(n):
    if n == 0:             # 1
        return 1           # если не 1
    nn = fact(n-1)*n         # вызываем функцию на 1 меньше и * на это число
    print(n,nn)
    return nn  
num = int(input("Задайте число:"))
print(fact(num))
