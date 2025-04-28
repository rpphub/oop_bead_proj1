from airline.airline import Airline
from flights.flight import Flight

class AirManager():
  def __init__(self,*airlines:Airline):
    self.airlines = list(airlines)

  def add_airline(self,*airlines:Airline):
    for airline in airlines:
      self.airlines.append(airline)

  def view_all_flight(self):
    print(f"{"Járatszám":{" "}^10}   {"Típus":{" "}^12}   {"Uticél":{" "}^8}   {"Ár(Ft)":{" "}^10}")

    for airline in self.airlines:
      #Légitársaságok
      for flight in airline.Flights:
        #Járatok
        print(f"{flight.flightNumber:{" "}^10}   {flight.type:{" "}^12}   {flight.dest:{" "}^8}   {flight.price:{" "}^10}")

  def get_flight_by_number(self,flightNumber:str) -> Flight:
    for airline in self.airlines:
      #Légitársaságok
      for flight in airline.Flights:
        #Járatok
        if(flightNumber == flight.flightNumber):
          return flight

  def __str__(self):
    return f"Társaságok száma: {len(self.airlines)}"