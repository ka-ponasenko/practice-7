N, K, R = map(int, input("Введите длину нити в 1 день, процент увеличения и необходимую длину нити через пробел: ").split())

count = 1

while N < R:
    count += 1
    N += N * (K / 100)

print(count)
