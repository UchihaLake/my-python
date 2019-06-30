def print_box(*args, **kwargs):
    for arg in args:
        print(arg)
    for name, item in kwargs.items():
        print(name, item)

title1 = 'Hello'
title2 = 'World'
title3 = 'Welcome'

print_box(title1, title2, title3,
          box_a = 'toys, books, pencils, bags',
          box_b = 'fruits, vegetables',
          box_c = 'wires, tools, materials')

