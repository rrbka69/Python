# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# import random

# # n = int(input())
# # list1=[random .randint (0,10) for _ in range (n)]

# list1 = [1, 1, 2, 0, -1, 3, 4, 4]
# count = 0
# list2 = []
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(len(list2))

numlist = [1, 1, 2, 0, -1, 3, 4, 4]
print(len(set(numlist)))
numlist2 = []





