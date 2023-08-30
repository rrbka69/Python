#  Задача №49.
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной


def show_menu():
    print('1. Распечатать справочник\n'
'2. Найти телефон по фамилии\n'
'3. Изменить номер телефона\n'
'4. Удалить запись\n'
'5. Найти абонента по номеру телефона\n'
'6. Добавить абонента в справочник\n'
'7. Закончить работу')
    choice=7
    s = input()
    if len(s)>=1 : # если вводится пустой стринг, то заканчиваем работу как при вводе 7
    # если введен не пустой стринг, то берем из него только первый символ
    # если первый символ не цифра от 1 до 7, то заканчиваем работу как при 7
        if s[0] in {'1','2','3','4','5','6','7'} :
            choice=int(s[0])
        return choice

def read_txt(filename):
    phone_book=[]
    #fieldsR=['Фамилия', 'Имя', 'Отчество', 'Телефон', 'Описание']
    fields=['LastName', 'Name1', 'Name2', 'TelNum', 'Comment']
    # with open('phonebook.txt','r',encoding='utf-8') as phb:
    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
            lst1= line.strip().split(',')
            for i in range(len(lst1)) :
                lst1[i]=lst1[i].strip() # вожможные лишние пробелы в начале и конце значений полей убираем
            record=dict(zip(fields,lst1))
            # при чтении желательно бы делать анализ данных: везде ли есть фамилия,
            # имеются ли лишние пробелы в начале и конце каждого поля, вообще: не испорчен ли файл со справочником
            phone_book.append(record)
            #print(record)
    return phone_book
def print_result(phone_book):
    for i in phone_book :
        print(i)
#
def find_by_lastname(phone_book,last_name) :
    last_n= last_name.strip()
#   print(last_n)
    shortList=[] # список тех записей, которые удовлетворяют условию
#   fields=['LastName', 'Name1', 'Name2', 'TelNum', 'Comment']
    for el in phone_book :
        if el['LastName']== last_n :
            #print(el)
            shortList.append(el)
    if len(shortList)==0 :
        print(last_n," в phone_book не обнаружен")
    else :
        print(last_n," в phone_book встречается ",len(shortList)," раз")
        for el in shortList :
            print(el)
            return shortList

def add_user(phone_book,user_data) : # на входе подаем список из пяти непустых стрингов
    fields=['LastName', 'Name1', 'Name2', 'TelNum', 'Comment']
    phone_book.append(dict(zip(fields,user_data)))
#
def find_by_number(phone_book,numberstr) :
    ns= numberstr.strip()
# print(ns)
    shortList=[] # список тех записей, которые удовлетворяют условию
    for el in phone_book :
        if el['TelNum']== ns :
            shortList.append(el)
    if len(shortList)==0 :
        print(ns," в phone_book не обнаружен")
    else :
        print(ns," в phone_book встречается ",len(shortList)," раз")
        for el in shortList :
            print(el)
    return shortList
# #
# def read_txt(filename):
# phone_book=[]
# fields=['Фамилия', 'Имя', 'Отчество', 'Телефон', 'Описание']
# with open('phonebook.txt','r',encoding='utf-8') as phb:
# for line in phb:
# record=dict(zip(fields,line.strip().split(',')))
# phone_book.append(record)
# print(record)
# return phone_book
#
def write_txt(filename,phone_book):
    with open('phonebook.txt','w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
    for v in phone_book[i].values():
        s+=v+','
    phout.write(f'{s[:-1]}\n') # из буферного стринга в файл записываем в строку всё кроме последнего знака
#
def change_number(phone_book,last_name,new_number) : # возвращаем список записей до изменения
    last_n= last_name.strip()
    shortList=[]
    flag=0
    flag2=0
    for el in phone_book :
        if el['LastName']== last_n :
            flag+=1
            print("Для записи")
            print(el)
            a=input("Вы действительно хотите заменить телефонный номер?: Y/N ").upper()
            if a=="Y" :
                shortList.append()
                flag2 +=1
                el['TelNum']=new_number
    if flag==0 :
        print(last_n," в phone_book не обнаружен")
    else :
        print(last_n," в phone_book встречается ",flag," раз, сделано ",flag2," замен")
    return shortList
def delete_by_lastname(phone_book,last_name) : # возвращаем список удаленных записей
    last_n= last_name.strip()
    flag=0
    flag2=0
    shortList=[]
    for el in phone_book :
        if el['LastName']== last_n :
            flag+=1
            print("Запись")
            print(el)
            a=input("вы действительно хотите удалить?: Y/N ").upper()
            if a=="Y" :
                shortList.append(el)
    flag2 +=1
    phone_book.remove(el)
    if flag==0 :
        print(last_n," в phone_book не обнаружен")
    else :
         print(last_n," в phone_book встречался ",flag," раз, удалено ",flag2," записей")
    #print(shortList)
    return shortList

def work_with_phonebook():
    choice=show_menu()
    phone_book=read_txt('phonebook.txt')
    while (choice!=7):
        if choice==1:
            print_result(phone_book)
        elif choice==2:
            fio=""
            while len(fio)==0 :
                fio=str(input('Фамилия ').strip())
            last_name=fio
            print(last_name)
            find_by_lastname(phone_book,last_name)
        elif choice==3:
            last_name=input('Фамилия ')
            new_number=input('new number:= ')
            print(change_number(phone_book,last_name,new_number))
            write_txt('phonebook.txt',phone_book)
        elif choice==4:
            lastname=input('lastname ')
            print(delete_by_lastname(phone_book,lastname))
            write_txt('phonebook.txt',phone_book)
        elif choice==5:
            number=input('number ')
            print(find_by_number(phone_book,number))
        elif choice==6:
            user_datas=input('new data (Фамилия Имя Отчество Телефон Комментарий) ')
            user_data = user_datas.split()
            if len(user_data)==5 :
                add_user(phone_book,user_data)
                write_txt('phonebook.txt',phone_book)
        else :
            print("данных не достаточно")
        choice=show_menu()
work_with_phonebook