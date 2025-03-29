N = int(input("Загадайте любое число: "))
count = 0
while N>1:
    N = (N+1)//2
    count+=1
print(count)
