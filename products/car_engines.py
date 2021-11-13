import abc


class CarEngineInterface(abc.ABC):
    @property
    def model(self) -> str:
        pass

    @abc.abstractmethod
    def start(self) -> str:
        pass

    @abc.abstractmethod
    def stop(self) -> str:
        pass


class CarEngineA(CarEngineInterface):
    def __init__(self) -> None:
        self._model = 'A'

    @property
    def model(self) -> str:
        return self._model

    def start(self) -> str:
        return f'Motor {self.model} ligado.'

    def stop(self) -> str:
        return f'Motor {self.model} desligado.'


class CarEngineB(CarEngineInterface):
    def __init__(self) -> None:
        self._model = 'B'

    @property
    def model(self) -> str:
        return self._model

    def start(self) -> str:
        return f'Motor {self.model} ligado.'

    def stop(self) -> str:
        return f'Motor {self.model} desligado.'
