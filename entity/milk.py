# class Milk:
#     def __init__(self, volume=0, fat=0, money=0):
#         self.__volume = volume
#         self.__fat = fat
#         self.__money = money
#
#     @property
#     def volume(self):
#         return self.__volume
#
#     @property
#     def fat(self):
#         return self.__fat
#
#     @property
#     def cost(self):
#         return self.__cost
#
#     @volume.setter
#     def diameter(self, volume):
#         self.__volume = volume
#
#     @fat.setter
#     def diameter(self, fat):
#         self.__fat = diameter
#
#     @diameter.setter
#     def diameter(self, diameter):
#         self.__diameter = diameter
#
#         df
#         __str__(self):
#         return (f"Orange: diamter = {self.__diameter}, "
#                 f"vitamin = {self.__vitamin}, "
#                 f"cost = {self.__cost}")

from entity.product import Product


class Milk(Product):
    def __init__(self, volume=0, fat=0, money=0):
        super().__init__(money)
        self.__volume = volume
        self.__fat = fat
        # self.__money = money

    @property
    def volume(self):
        return self.__volume

    @property
    def fat(self):
        return self.__fat

    # @property
    # def money(self):
    #     return self.__money

    @volume.setter
    def volume(self):
        return self.__volume

    @fat.setter
    def fat(self, fat):
        self.__fat = fat

    # @money.setter
    # def money(self, money):
    #     self.__money = money

    def __str__(self):
        return (f"Milk: volume = {self.__volume}, "
                f"fat = {self.__fat}, "
                f"money = ${self.price}")
