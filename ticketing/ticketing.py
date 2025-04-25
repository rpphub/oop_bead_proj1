from airline.manager import AirManager

class Tickets:
  def __init__(self):
    self.tickets = []
  
  def buy(self,flightNumber:int):
    self.tickets.append(flightNumber)

  def cancel(self,flightNumber:int):
    self.tickets.remove(flightNumber)

  def view(self,AirMan:AirManager):
    print("Lefoglalt jegyek:")
    print(f"{"Járatszám":{" "}^10}   {"Típus":{" "}^12}   {"Uticél":{" "}^8}   {"Ár":{" "}^10}")
    for ticket in self.tickets:
      flight = AirMan.get_flight_by_number(ticket)
      print(f"{flight.flightNumber:{" "}^10}   {flight.type:{" "}^12}   {flight.dest:{" "}^8}   {flight.price:{" "}^10}")
