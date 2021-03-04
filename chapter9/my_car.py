from car import Car
from electric_car import ElectricCar as EC

my_beetle = Car('volswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tela = EC('tesla', 'roadster', 2019)
print(my_tela.get_descriptive_name())
