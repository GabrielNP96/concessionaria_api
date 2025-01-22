import pytest
from src.models.car.Car import Car
from src.models.motorcycle.Motorcycle import Motorcycle

# Teste da classe Car
def test_car_creation():
    car = Car("Fusca", "Volkswagen", 1960, "Gasolina", 1.3)
    
    assert car.model == "Fusca"
    assert car.manufacturer == "Volkswagen"
    assert car.year == 1960
    assert car.type_of_fuel == "Gasolina"
    assert car.engine == 1.3

def test_car_invalid_engine():
    with pytest.raises(ValueError):
        Car("Fusca", "Volkswagen", 1960, "Gasolina", -1)

def test_car_vehicle_data():
    car = Car("Fusca", "Volkswagen", 1960, "Gasolina", 1.3)
    data = car.vehicle_data()
    assert "Modelo: Fusca" in data
    assert "Fabricante: Volkswagen" in data
    assert "Ano: 1960" in data
    assert "Tipo de combustivel: Gasolina" in data
    assert "Motor: 1.3" in data

# Teste da classe Motorcycle
def test_motorcycle_creation():
    motorcycle = Motorcycle("Honda CB 500", "Honda", 2020, "Gasolina", 500)
    
    assert motorcycle.model == "Honda CB 500"
    assert motorcycle.manufacturer == "Honda"
    assert motorcycle.year == 2020
    assert motorcycle.type_of_fuel == "Gasolina"
    assert motorcycle.displacement == 500

def test_motorcycle_invalid_displacement():
    with pytest.raises(ValueError):
        Motorcycle("Honda CB 500", "Honda", 2020, "Gasolina", 40)

def test_motorcycle_vehicle_data():
    motorcycle = Motorcycle("Honda CB 500", "Honda", 2020, "Gasolina", 500)
    data = motorcycle.vehicle_data()
    assert "Modelo: Honda CB 500" in data
    assert "Fabricante: Honda" in data
    assert "Ano: 2020" in data
    assert "Tipo de combustivel: Gasolina" in data
    assert "Cilindradas: 500" in data
