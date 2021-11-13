from factories.car_factories import CarFactoryInterface

def factory_client(factory: CarFactoryInterface):
    chassis = factory.make_chassis()
    engine = factory.make_engine()

    print(chassis.connect_engine(engine))
    print(engine.start())
    print(engine.stop())
    print()
