
# переделать простое число или составное
def celoechislo (a):
    if a % 2 == 0: #проверяем четное ли число
        return False
    d = 3
    while d*d<= a and a %d!=0: # если число не четное 
        d+=2
    return d*d>a
a = int(input('введите число:'))
prim = celoechislo(a)
message = ("составное", "простое")[prim]
print (message)




 