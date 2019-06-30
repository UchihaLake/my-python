from functools import wraps


def add_boxA(item):
    @wraps(item)
    def put_itemA():
        return 'put {} to boxA'.format(item())
    return put_itemA


def add_attribute(stat):
    def add_box1(item):
        def put_item1():
            return 'put {} to box1 {}'.format(item(), stat)
        return put_item1
    return add_box1


def add_box2(item):
    def put_item2():
        return 'put {} to box2'.format(item())
    return put_item2


@add_attribute('carefully')
def new_toy():
    return 'a new toy'


@add_boxA
@add_box2
def new_ball():
    return 'a new ball'


print(new_toy())
print(new_ball())

print(new_toy.__name__)

