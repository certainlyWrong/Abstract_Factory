import client
from factories.car_factories import CarFactoryA, CarFactoryB


if __name__ == '__main__':
    client.factory_client(CarFactoryA())
    client.factory_client(CarFactoryB())
