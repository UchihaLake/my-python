def new_gen():
    yield 'Hello'
    yield 'World'
    yield 'Mike'


def loop_gen():
    for a in range(10):
        for b in range(10):
            for c in range(10):
                yield (a, b, c)


res = (3, 4, 5)
for (a1, b1, c1) in loop_gen():
    print(a1, b1, c1)
    if (a1, b1, c1) == res:
        print('Found {}'.format((a1, b1, c1)))
        break
