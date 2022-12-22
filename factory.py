from enum import Enum


class SushiType(Enum):
    Philadelphia = 0,
    California = 1,
    Ebitempura = 2


class Sushi:
    def __init__(self, price: float):
        self.__price = price

    def get_price(self) -> float:
        return self.__price


class SushiPhiladelphia(Sushi):
    def __init__(self):
        super().__init__(395)


class SushiCalifornia(Sushi):
    def __init__(self):
        super().__init__(385)


class SushiEbitempura(Sushi):
    def __init__(self):
        super().__init__(320)


def create_sushi(sushi_type: SushiType) -> Sushi:
    factory_dict = {
        SushiType.Philadelphia: SushiPhiladelphia,
        SushiType.California: SushiCalifornia,
        SushiType.Ebitempura: SushiEbitempura
    }
    return factory_dict[sushi_type]()


if __name__ == "__main__":
    for sushi in SushiType:
        my_sushi = create_sushi(sushi)
        print(f'Sushi type: {sushi}, price: {my_sushi.get_price()}')