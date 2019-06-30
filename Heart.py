def heart(n):
    m = int(n / 2 + 1)
    spc = round(n / 4)
    temp = 0

    for j in range(spc - temp * 2):
        for i in range(spc - j):
            print(' ', end='')
        for i in range(spc + j):
            print('*', end='')
        for i in range(spc - j):
            print(' ',end='')
        for i in range(spc + j):
            print('*', end='')
        temp = j
        print()

    for i in range(n):
        for j in range(i):
            print(' ', end='')
        for j in range(n - i * 2):
            print('*', end='')
        print()


if __name__ == '__main__':
    heart(9)
