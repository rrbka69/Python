# определить является ли слово палиндромом

# word = 1234321
# def str(word):
#     if str(word):    
#         return str(word)[::-1] == str(word)
#     print ('{} - полиндром'.format(word))
#     else:
#     print ('{} - не полиндром'.format(word))

def str(word):
    if len(word)<=1:
        return True
    # return str(word[len(word)-1]) and (word[0] == word [len(word)-1])  1 решение 
    # return str(word[1:-1]) and (word[0] == word [-1])                  2 решение
    elif word [0] == word[-1]:
        return str(word[1:-1])
    else:
        return False                  #                                  3 решение

ss = input("введите слово:=")
print(str(ss))
