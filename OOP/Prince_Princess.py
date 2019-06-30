class Prince:
    def __init__(self, money, wisdom, power):
        self.__money = money
        self.__wisdom = wisdom
        self.__power = power

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, money):
        self.__money = money

    @property
    def wisdom(self):
        return self.__wisdom

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, power):
        self.__power = power

    def output(self):
        for i in (self.__money, self.__wisdom, self.__power):
            print(i)


class Business:
    def __init__(self):
        self.__price = int(input('How much is the price ?'))
        self.__amount = int(input('How many ?'))

    def decrease_money(self, money):
        return money - self.__price * self.__amount

    def can_pass(self, prince_stat):
        if prince_stat.money >= self.__price * self.__amount:
            prince_stat.money = self.decrease_money(prince_stat.money)
            return prince_stat, True
        return prince_stat, False


class Academic:
    def __init__(self):
        self.__wisdom = int(input('How difficult is the question ?'))

    def can_pass(self, prince_stat):
        if prince_stat.wisdom >= self.__wisdom:
            return prince_stat, True
        return prince_stat, False


class Power:
    def __init__(self):
        self.__power = int(input('How strong is the soldier ?'))

    def decease_power(self, power):
        return power - self.__power

    def can_pass(self, prince_stat):
        if prince_stat.power >= self.__power:
            prince_stat.power = self.decease_power(prince_stat.power)
            return prince_stat, True
        return prince_stat, False


class Gates:
    def __init__(self, n):
        self.__n = n
        self.__n_gates = []
        for i in range(self.__n):
            __type = int(input('1.Business\n2.Academic\n3.Power\n'))
            if __type == 1:
                self.__n_gates.append(Business())
            elif __type == 2:
                self.__n_gates.append(Academic())
            elif __type == 3:
                self.__n_gates.append(Power())

    def can_pass(self, prince_stat):
        for i in range(self.__n):
            prince_stat, __is_pass = self.__n_gates[i].can_pass(prince_stat)
            if not __is_pass:
                return False
        return True


def input_prince():
    __prince_money = int(input('How much money the prince have ?'))
    __prince_wisdom = int(input('How smart the prince is ?'))
    __prince_power = int(input('How strong is the prince ?'))
    return __prince_money, __prince_wisdom, __prince_power


def input_gates():
    __n = int(input('How many gates do you want ?'))
    return __n


if __name__ == '__main__':
    prince_money, prince_wisdom, prince_power = input_prince()
    prince = Prince(prince_money, prince_wisdom, prince_power)
    n = input_gates()
    gates = Gates(n)
    if gates.can_pass(prince):
        prince.output()
        print('The prince saves the princess, Congratulation!!')
    else:
        print('Oh no the prince does not strong enough!!')
