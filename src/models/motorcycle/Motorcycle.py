from src.models.Vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, model: str, manufacturer: str, year: int, type_of_fuel: str, displacement: int):
        super().__init__(model, manufacturer, year, type_of_fuel)
        self.displacement = displacement

    @property
    def displacement(self):
        return self._displacement
    
    @displacement.setter
    def displacement(self, value: int):
        if value < 50:
            raise ValueError("As cilindradas não podem ser menores que 50")
        self._displacement = value

    def vehicle_data(self):
        return(f"""Modelo: {self.model}
Fabricante: {self.manufacturer}
Ano: {self.year}
Tipo de combustivel: {self.type_of_fuel}
Cilindradas: {self.displacement}""")
    


# Criando uma motocicleta
motorcycle = Motorcycle("Honda CB 500", "Honda", 2020, "Gasolina", 500)

# Exibindo os dados da motocicleta
print(motorcycle.vehicle_data())
