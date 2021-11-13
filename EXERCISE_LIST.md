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
