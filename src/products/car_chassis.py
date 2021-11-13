import abc

from products.car_engines import CarEngineInterface


class CarChassisInterface(abc.ABC):
    @property
    def model(self) -> str:
        pass

    @abc.abstractmethod
    def connect_engine(self, engine: CarEngineInterface) -> str:
        pass


class CarChassisA(CarChassisInterface):
    def __init__(self) -> None:
        self._model = 'A'

    @property
    def model(self) -> str:
        return self._model

    def connect_engine(self, engine: CarEngineInterface) -> str:
        if isinstance(engine, CarEngineInterface) and engine.model == self.model:
            return f'Motor modelo {engine.model} conectado ao chassi {self.model}.'
        return f'Motor impróprio para o chassi {self.model}.'


class CarChassisB(CarChassisInterface):
    def __init__(self) -> None:
        self._model = 'B'

    @property
    def model(self) -> str:
        return self._model
    
    def connect_engine(self, engine: CarEngineInterface) -> str:
        if isinstance(engine, CarEngineInterface) and engine.model == self.model:
            return f'Motor modelo {engine.model} conectado ao chassi {self.model}.'
        return f'Motor impróprio para o chassi {self.model}.'
