# Вводятся номера телефонов в одну строчку через пробел с разными кодами стран
# +7, +6, +2, +4 и т.д. Необходимо составить словарь d, где ключи - это коды +7, +6 , +2.., 
# а значения - список номеров (след в том же порядке, что и во входной строке) с соосветствующими кодами. 
# Полученный словарь вывести командой: 
#  print(*sorted(d.items()))

tel = '+7235689, +78984545, +6987456, +5894563, +289456123, +48974561'.split()
a = {}
for i in tel:
    key = i[:2]
    print(key)
    if key not in a:
        a[key] = [i]  # i записываем в значение ключа
    else:
        a [key] += [i]   # a = список
print(a)



 