# if 5 > 3:
#     print (1)
# print (5>3)



# def func(x):
#     if x>5:
#         return True
# print(func(10))


# if func(10):
#     print(1)


# def fun1(x):
#     return x
# print(fun1(5))


# fun2 = lambda x: x 
# print(fun2(5))


# print ((lambda x: x )(5))



# def fun1(x,y):
#     return x+y
# print(fun1(5,3))


# fun2 = ((lambda x,y: x+y)(5,3))
# print(fun1(5,3))


# print((lambda x,y: x+y)(5,3))


str1 = "3 4 3 7 9 1"
print(str1)

lst1 = str1.split()
print(lst1)


lst2 = list(map(int,lst1))
print(lst2)

fun3 = lambda x: x*1,8,
print(lst2)

lst3 = list(map(lambda x: x *1,8, lst2))
print(lst3)
lst3  = list(map(fun3 ,lst2))

print(lst3)

lst4 = list (filter(lambda x: x, lst2))