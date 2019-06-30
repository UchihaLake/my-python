a = int(input())
b = int(input())
i = 1
count = 0
if a == 0:
    _min = b
elif b == 0:
    _min = a
else:
    _min = min(a, b)
while i <= _min:
    if a % i == 0 and b % i == 0:
        count += 1
    i += 1
print(count)
