from src.models.Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, model: str, manufacturer: str, year: int, type_of_fuel: str, engine: float):
        super().__init__(model, manufacturer, year, type_of_fuel)
        self.engine = engine

    # Getter e Setter para o motor
    @property
    def engine(self):
        return self._engine
    
    @engine.setter
    def engine(self, value: float):
        if value <= 0:
            raise ValueError("O tamanho do motor deve ser maior que zero.")
        self._engine = value

    def vehicle_data(self):
        return(f"""Modelo: {self.model}
Fabricante: {self.manufacturer}
Ano: {self.year}
Tipo de combustivel: {self.type_of_fuel}
Motor: {self.engine}""")
    
# Criando um veículo (carro)
car = Car("Fusca", "Volkswagen", 1960, "Gasolina", 1.3)

# Exibindo os dados do carro
print(car.vehicle_data())

