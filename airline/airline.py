from flights.flight import Flight

class Airline():
  def __init__(self,name:str,*flights:Flight):
    self.name = name
    self.Flights = list(flights)

  def __str__(self):
    return f"Társaság neve: {self.name} | Járatok összesen: {len(self.Flights)}"