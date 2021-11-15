class ItemDiscount:
    def __init__(self, name, price):
        # self.__name = name
        # self.__price = price
        self.name = name
        self.price = price

    def get_name(self):
        # return self.__name
        return self.name

    def get_price(self):
        # return self.__price
        return self.price

    def set_price(self, price):
        # self.__price = price
        self.price = price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price, discount):
        ItemDiscount.__init__(self, name, price)
        self.discount = discount

    def get_info(self):
        print(f' название товара - {self.get_name()}')

    def __str__(self):
        return f'{self.get_price() - self.discount}'

    def get_parent_data(self):
        print(f'наименование товара - {self.name}, цена - {self.price}')


class ItemDiscountReportSecond(ItemDiscount):
    def get_info(self):
        print(f' цена товара - {self.get_price()}')


goods1 = ItemDiscount('clevo', 1000)
goods2 = ItemDiscountReport('msi', 1000, 200)
goods3 = ItemDiscountReportSecond('Asus', 5000)
print(f'имя товара - {goods1.get_name()}, цена товара - {goods1.get_price()}')

goods2.get_parent_data()
goods2.set_price(2350)
print(f'цена товара после изменения - {goods2.get_price()}')

print(f'цена товара со скидкой - {goods2}')
goods2 .get_info()
goods3 .get_info()


def obj_handler(obj):
    obj.get_info()


obj_handler(goods2)
obj_handler(goods3)

for obj in (goods2, goods3):
    print(f'получение данных через цикл - ', end='')
    obj.get_info()
    