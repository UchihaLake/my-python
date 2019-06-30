class Gold:
    def __init__(self):
        self.__sect_name = 'kim'
        self.__sect = ['Thieu Lam', 'Thien Vuong Bang']

    @staticmethod
    def mutual_opposition(sect):
        if sect == 'hoa':
            return -2
        elif sect == 'moc':
            return  2
        elif sect == 'tho':
            return -1
        elif sect == 'thuy':
            return 1

    @property
    def name(self):
        return self.__sect_name


class Carpentry:
    def __init__(self):
        self.__sect_name = 'moc'
        self.__sect = ['Ngu Doc Giao', 'Duong Mon']

    @staticmethod
    def mutual_opposition(sect):
        if sect == 'kim':
            return -2
        elif sect == 'tho':
            return 2
        elif sect == 'thuy':
            return -1
        elif sect == 'hoa':
            return 1

    @property
    def name(self):
        return self.__sect_name


class Water:
    def __init__(self):
        self.__sect_name = 'thuy'
        self.__sect = ['Nga My', 'Thuy Yen Mon']

    @staticmethod
    def mutual_opposition(sect):
        if sect == 'tho':
            return -2
        elif sect == 'hoa':
            return 2
        elif sect == 'kim':
            return -1
        elif sect == 'moc':
            return 1

    @property
    def name(self):
        return self.__sect_name


class Fire:
    def __init__(self):
        self.__sect_name = 'hoa'
        self.__sect = ['Cai Bang', 'Thien Nhan Giao']

    @staticmethod
    def mutual_opposition(sect):
        if sect == 'thuy':
            return -2
        elif sect == 'kim':
            return 2
        elif sect == 'moc':
            return -1
        elif sect == 'tho':
            return 1

    @property
    def name(self):
        return self.__sect_name


class Earth:
    def __init__(self):
        self.__sect_name = 'tho'
        self.__sect = ['Con Lon', 'Vo Dang']

    @staticmethod
    def mutual_opposition(sect):
        if sect == 'moc':
            return -2
        elif sect == 'thuy':
            return 2
        elif sect == 'hoa':
            return -1
        elif sect == 'kim':
            return 1

    @property
    def name(self):
        return self.__sect_name


class Player:
    def __init__(self, level):
        self.__level = level
        __inp = input('Player Sect:')
        if __inp == 'hoa':
            self.__sect = Fire()
        elif __inp == 'kim':
            self.__sect = Gold()
        elif __inp == 'moc':
            self.__sect = Carpentry()
        elif __inp == 'thuy':
            self.__sect = Water()
        elif __inp == 'tho':
            self.__sect = Earth()

    @property
    def power(self):
        return self.__level * 5

    @property
    def sect(self):
        return self.__sect


class Monster:
    def __init__(self, level):
        self.__level = level
        __inp = input('Monster Element:')
        if __inp == 'hoa':
            self.__sect = Fire()
        elif __inp == 'kim':
            self.__sect = Gold()
        elif __inp == 'moc':
            self.__sect = Carpentry()
        elif __inp == 'thuy':
            self.__sect = Water()
        elif __inp == 'tho':
            self.__sect = Earth()
        self.__type = int(input('1.Thuong\n2.Dau Linh\n'))

    @property
    def power(self):
        if self.__type == 1:
            return self.__level * 3
        elif self.__type == 2:
            return self.__level * 7

    @property
    def sect(self):
        return self.__sect


class Sect:
    @staticmethod
    def compare(obj1, obj2):
        if obj1.sect.mutual_opposition(obj2.sect.name) == 2:
            stat1 = 0.2
            stat2 = -0.2
        elif obj1.sect.mutual_opposition(obj2.sect.name) == -2:
            stat1 = -0.2
            stat2 = 0.2
        elif obj1.sect.mutual_opposition(obj2.sect.name) == 1:
            stat1 = 0.1
        elif obj1.sect.mutual_opposition(obj2.sect.name) == -1:
            stat1 = -0.1
        if int(obj1.power) + int(obj1.power) * stat1 > int(obj2.power) + int(obj2.power) * stat2:
            print('1 manh hon 2')
        else:
            print('2 manh hon 1')


if __name__ == '__main__':
    y_lv = int(input('Player Level:'))
    m_lv = int(input('Monster level:'))
    player = Player(y_lv)
    mon1 = Monster(m_lv)
    cmp = Sect()
    cmp.compare(player, mon1)


