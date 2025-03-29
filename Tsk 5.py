x = int(input('Введите объем: '))
a = 1
d = []
while a**3<=x:
    d.append(a**3)
    a+=1
print(' '.join(map(str, d)))