a = input("Введите строку: ")
d = []
for x in a:
    d.append(x)
result = d[2::3]
print(''.join(result))
    