from entity.milk import Milk
from entity.orange import Orange
from entity.bread import Bread
from container.basket import Basket
from logic.shop_assistance import ShopAssistance


def main():
    basket = Basket()
    br = Bread("white", "second", 3.0)
    o = Orange(200, 300, 1.5)
    m = Milk(1, 4.2, 5.5)

    basket.add(br)
    basket.add(o)
    basket.add(m)

    # print(f"size = {basket.size}")

    print(basket)

    total = ShopAssistance.calculate_total_price(Basket)

    # for i in range(basket.size):
    #     print(basket.get_product(i))
    # #
    # print(br)
    # print(o)
    # print(m)


if __name__ == "__main__":
    main()
