from entity.milk import Milk
from entity.orange import Orange
from entity.bread import Bread




def main():
    br = Bread()
    o = Orange()
    m = Milk(1, 4.2, 5.5)

    print(br)
    print(o)
    print(m)


if __name__ == "__main__":
    main()