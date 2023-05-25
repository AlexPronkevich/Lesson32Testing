from entity.product import Product


class Orange(Product):
    def __init__(self, diameter=100, vitamin=1000, cost=0):
        super().__init__(cost)
        self.__diameter = diameter if diameter > 0 else 100

        self.__vitamin = vitamin if vitamin > 0 else 0
        # self.__cost = cost Вместо этой строки  super....

    @property
    def diameter(self):
        return self.__diameter

    @property
    def vitamin(self):
        return self.__vitamin

    # @property
    # def cost(self):
    #     return self.__cost

    @diameter.setter
    def diameter(self, diameter):
        if diameter > 0:
            self.__diameter = diameter

    @vitamin.setter
    def vitamin(self, vitamin):
        if vitamin > 0:
            self.__vitamin = vitamin

    # @cost.setter
    # def cost(self, cost):
    #     self.__cost = cost

    def __str__(self):
        return (f"Orange: diameter = {self.__diameter}, "
                f"vitamin = {self.__vitamin}, "
                f"cost = ${self.price}")
