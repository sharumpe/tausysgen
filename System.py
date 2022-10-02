from random import randint
from random import choice
from tokenize import String
from Temperament import Temperament
from Planet import Planet

class System:
  name = "foo"
  temperament = "bar"
  system_size = 0
  planets = list()

  def __init__(self, name) -> None:
    self.name = name
    self.temperament = Temperament()
    self.system_size = randint(2,6) + 2
    _planets = list()
    for x in range(self.system_size):
      _planets.append(choice(Planet.planets))
    self.planets = _planets

  def __str__(self) -> str:
    retval = f"""
System: {self.name}
  Temperament: {self.temperament}
  Planets:
"""
    for planet in self.planets:
      retval += f"    {planet}\n"
    
    return retval

