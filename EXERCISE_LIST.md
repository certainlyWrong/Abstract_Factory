## Universidade Federal do Piauí - UFPI

## Campus Senador Helvídio Nunes de Barros - CSHNB

## Disciplina: Programação Orientada a Objetos

## Professor: Flávio Henrique Duarte de Araújo

### Equipe:

- Adriano Rodrigues (20209000789)
- Armando Borges (20209019717)
- Hudson Bandeira (20179147166)
- Luís Clício (20209006970)

## Lista de exercícios sobre **Abstract Factory Pattern**

1. As classes concretas dos motores de modelos 'A' e 'B' implementam a interface
   `CarEngineInterface`, porém ela ainda não foi criada. Sua tarefa é criá-la para
   definir um contrato entre as partes que utilizam objetos do tipo "motor de carro".

- Classe que define o motor de modelo 'A':

  	```python
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
  	```

- Classe que define o motor de modelo 'B':

  	```python
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
  	```

- Interface `CarEngineInterface`:

  ```python
  # Crie o código da interface aqui
  ```

2. Agora, vamos fazer o mesmo para o chassi do carro. As classes concretas dos chassis
  de modelos 'A' e 'B' implementam a interface `CarChassisInterface`, porém ela ainda 
  não foi criada. Sua tarefa é criá-la para definir um contrato entre as partes que 
  utilizam objetos do tipo "chassi do carro".

- Classe que define o chassi de modelo 'A':

  	```python
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
  	```

- Classe que define o chassi de modelo 'B':
  
  	```python
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
    ```
    
- Interface `CarEngineInterface`:

  ```python
  # Crie o código da interface aqui
  ```

3. As classes concretas das fábricas estão com alguns erros de semântica, corrija-as
   de acordo com a interface `CarFactoryInterface`, bem como faça com que elas
	 criem os produtos corretos. Lembre-se que fábricas produzem peças para um único
	 modelo de carro.
   
- Interface:
  
  	```python
	class CarFactoryInterface(abc.ABC):
		@abc.abstractmethod
		def make_chassis(self) -> CarChassisInterface:
			pass

		@abc.abstractmethod
		def make_engine(self) -> CarEngineInterface:
			pass
  	```

- Classes concretas:

	```python
	class CarFactoryA(CarFactoryInterface):
		def make_chassis(self) -> CarEngineInterface:
			return CarChassisA()

		def make_engine(self) -> CarChassisInterface:
			return CarEngineB()


	class CarFactoryB(CarFactoryInterface):
		def make_chassis(self) -> CarChassisInterface:
			return CarChassisA()

		def make_engine(self) -> CarChassisInterface:
			return CarEngineB()
  	```

- Correção:

  ```python
  # Corrija o código aqui
  ```
