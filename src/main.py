from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, model: str, manufacturer: str, year: int, type_of_fuel: str, engine: float):
        self.model = model
        self.manufacturer = manufacturer
        self.year = year
        self.type_of_fuel = type_of_fuel
        self.engine = engine

    # Getter e Setter para o modelo
    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, value: str):
        if len(value) == 0:
            raise ValueError("O modelo não pode ser vazio.")
        self._model = value

    # Getter e Setter para o fabricante
    @property
    def manufacturer(self):
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self, value: str):
        if len(value) == 0:
            raise ValueError("O fabricante não pode ser vazio.")
        self._manufacturer = value

    # Getter e Setter para o ano
    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value: int):
        if value < 1886:  # O primeiro carro foi criado em 1886
            raise ValueError("Ano inválido. O ano deve ser maior ou igual a 1886.")
        self._year = value

    # Getter e Setter para o tipo de combustível
    @property
    def type_of_fuel(self):
        return self._type_of_fuel
    
    @type_of_fuel.setter
    def type_of_fuel(self, value: str):
        valid_fuels = ["Gasolina", "Álcool", "Diesel", "Elétrico"]
        if value not in valid_fuels:
            raise ValueError(f"Tipo de combustível inválido. Valores válidos: {', '.join(valid_fuels)}.")
        self._type_of_fuel = value

    # Getter e Setter para o motor
    @property
    def engine(self):
        return self._engine
    
    @engine.setter
    def engine(self, value: float):
        if value <= 0:
            raise ValueError("O tamanho do motor deve ser maior que zero.")
        self._engine = value

    @abstractmethod
    def vehicle_data(self):
        #deve exibir dados do carro ou moto
        pass
