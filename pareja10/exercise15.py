from functions import getCity
from functions import getState
from functions import getPeopleInStateAmmount

cities = [["Rosario","Santa Fe"], ["Carlos Paz","Córdoba"], ["Balcarce","Buenos Aires"], ["Cosquín","Córdoba"]]
people = [["Juan Perez",26782345,"Carlos Paz"], ["María Gomez",40173542,"Rosario"], ["Ana Ríos",9216378,"Cosquín"]] 

"""
Checking getCity function
"""
print("City: ", getCity(people, 26782345))
print("City: ", getCity(people, 12345678))

"""
Checking getState function
"""
print("State: ", getState(people, cities, 9216378))
print("State: ", getState(people, cities, 12345678))

"""
Checking getPeopleInStateAmmount function
"""
print("Pople ammount living in Cordoba", getPeopleInStateAmmount(people, cities, "Córdoba"))
print("Pople ammount living in Santa Fe", getPeopleInStateAmmount(people, cities, "Santa Fe"))
print("Pople ammount living in San Luis", getPeopleInStateAmmount(people, cities, "San Luis"))