import abc

from products.car_chassis import CarChassisInterface, CarChassisA, CarChassisB
from products.car_engines import CarEngineInterface, CarEngineA, CarEngineB


class CarFactoryInterface(abc.ABC):
    @abc.abstractmethod
    def make_chassis(self) -> CarChassisInterface:
        pass

    @abc.abstractmethod
    def make_engine(self) -> CarEngineInterface:
        pass


class CarFactoryA(CarFactoryInterface):
    def make_chassis(self) -> CarChassisInterface:
        return CarChassisA()

    def make_engine(self) -> CarEngineInterface:
        return CarEngineA()


class CarFactoryB(CarFactoryInterface):
    def make_chassis(self) -> CarChassisInterface:
        return CarChassisB()

    def make_engine(self) -> CarEngineInterface:
        return CarEngineB()
