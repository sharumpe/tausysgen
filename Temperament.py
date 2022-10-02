from random import randint

class Temperament:
  types = {
    "Warlike": "Add 1 to the Military Power of each planet in this star system.",
    "Prideful": "You cannot use the Show of Force Requisition (p84) while assimilating this star system.",
    "Idealogues": "Add 1 to the Diplomat Power of each planet in this star system.",
    "Trade Contacts": "Select 1 planet and halve its Diplomat Power (rounding up).",
    "Corrupt and Decadent": "Add 2 to the Diplomat Power of this star system's Core World.",
    "Dictatorship": "Add 2 to the Military Power of this star system's Core World."
  }

  def __init__(self):
    self.type = randint(0,5)
  
  def __str__(self) -> str:
    return f"{list(Temperament.types.keys())[self.type]}"

class Planet:
  types = {

  }