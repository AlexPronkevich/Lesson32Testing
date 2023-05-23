from entity.product import Product


class Basket:
    def __init__(self, products=None):
        if not products:
            self.__products = []
        else:
            self.__products = products

        # if products:
              #self.__products

    # def get_size(self):
    #     return len(self.__products)

    @property  # Это свойство вместо метода выше
    def size(self):
        return len(self.__products)

    def get_product(self, index):
        if (isinstance(index, int) and
                index >= 0 and index < self.size):
            return self.__products[index]

    def add(self, product):
        if isinstance(product, (Bread, Milk, Orange)):
            self.__products.append(product)

    def __str__(self):
        msg = "List of products:"

        for i in range(self.size):
            msg += f"\n{i + 1} " + str(self.__products[i])

        return msg
