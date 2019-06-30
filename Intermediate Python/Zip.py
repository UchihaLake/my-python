x = [0, 5, 3, 1]
y = [3, 4, 5, 7, 8]
z = [2, 5, 5, 7]

for i, j, a in zip(x, y, z):
    print(i, j, a)

for i in zip(y):
    print(i)

for i in zip(x, y, z):
    print(i)

[print(zip(x, y, z))]
print(list(zip(x, y, z)))