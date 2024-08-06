class Car:
    def get_brand(self):
        return "Марка автомобиля"


class Tesla(Car):
    def get_brand(self):
        return "Tesla"


def main():

    car = Car()
    print("Car brand:", car.get_brand())

    tesla = Tesla()
    print("Tesla brand:", tesla.get_brand())


if __name__ == "__main__":
    main()
