d = set()
for x in range(100, 1000):
    if x % 17 == 0:
        d.add(x)

print(" ".join(map(str, sorted(d))))

print(len(d))