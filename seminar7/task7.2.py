#  с помощью лямбда и фильтра составить список из двух значных чисел. ввод "2 10 -32 8 1 78", вывод [10, -32, 78]
#  ["10", "-32", "78"]

list1 = [10, 0, -32, 7, 78]
list2 = '10 0 -32 7 78'
# listRes2 = list(filter(lambda x: 9<abs(x)<100,map(int,list2.split())))
# print(listRes2)

list3 = list(filter(lambda x: len(str(abs(int(x))))==2, list2.split()))
print(list3)