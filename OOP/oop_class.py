class Food:
    stt = 1
    so_thu_tu = 1
    ingredient = 'tomato'

    def __init__(self, name, category, price, rating):
        self.name = name
        self.category = category
        self.price = price
        self.rating = rating
        self.stt = Food.so_thu_tu
        Food.so_thu_tu += 1

    def food_name(urself, str):
        return urself.name + str

    def food_amount(self):
        return self.number

    @staticmethod
    def print_hello():
        print("Hello")

    @staticmethod
    def print_goodbye():
        print("goodbye")


class Ham(Food):
    def __init__(self, name, category, price, rating, ham_amount):
        super().__init__(name, category, price, rating)
        self.ham = ham_amount


pizza = Food('Pizza', 'main', 300, 4)
beacon = Food('Beacon', 'main', 200, 5)
pizza.print_goodbye()
ham = Ham('Ham', 'optional', 300, 4, 2)
print(ham.food_name('hh'))
