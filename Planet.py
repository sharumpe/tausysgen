class Planet:
  planets = []

  @staticmethod
  def build_planets():
    return [
      Planet("Shrine World",5,2),
      Planet("Mining World",3,4),
      Planet("Civilian World",3,2),
      Planet("Military Base",4,5),
      Planet("Fleet Installation",5,5),
      Planet("Agri World",2,2),
      Planet("Political Center",6,3),
      Planet("Trader's Hub",4,4),
      Planet("Research World",4,3)
    ]
  
  def __init__(self, name, dp, mp) -> None:
    self.name = name
    self.diplomat_power = dp
    self.military_power = mp

  def __str__(self) -> str:
    return f"{self.name}: DP: {self.diplomat_power}; MP: {self.military_power}"

Planet.planets = Planet.build_planets()