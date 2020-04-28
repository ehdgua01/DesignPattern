import abc


class CaffeineBeverage(abc.ABC):
    def prepare_recipe(self) -> None:
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self) -> None:
        print("물 끓이는 중")

    def pour_in_cup(self) -> None:
        print("컵에 따르는 중")

    @abc.abstractmethod
    def brew(self) -> None:
        pass

    @abc.abstractmethod
    def add_condiments(self) -> None:
        pass
