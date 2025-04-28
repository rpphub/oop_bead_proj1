from airline.manager import AirManager

class Tickets:
  def __init__(self,*tickets):
    self.tickets = list(tickets)
  
  def buy(self,AirMan:AirManager, name:str, flightNumber:str):
    flight = AirMan.get_flight_by_number(flightNumber)
    if(flight == None):
      print(f"Nem létezik ez a járatszám({flightNumber})")
      print()
      return
    
    self.tickets.append({
        "name": name,
        "flightNumber": flightNumber
    })
    print("Foglalás történt")
    print(f"{"Neve":{" "}^20}  {"Járatszám":{" "}^10}   {"Típus":{" "}^12}   {"Uticél":{" "}^8}   {"Ár(Ft)":{" "}^10}")
    print(f"{name:{" "}^20} {flightNumber:{" "}^10}   {flight.type:{" "}^12}   {flight.dest:{" "}^8}   {flight.price:{" "}^10}")

  def cancel(self,AirMan:AirManager, index:int):
    try:
      ticket = self.tickets[index]
    except:
      print("Nincs ilyen foglalás, vagy hibás azonosító.")
      return
    
    print("Biztos törölni akarja a következő foglalást ?(I/N)")
    print(f"{"Azonosító":{" "}^8} {"Neve":{" "}^20}  {"Járatszám":{" "}^10}   {"Típus":{" "}^12}   {"Uticél":{" "}^8}   {"Ár(Ft)":{" "}^10}")
    flight = AirMan.get_flight_by_number(ticket['flightNumber'])
    print(f"{index:{" "}^8} {ticket['name']:{" "}^20} {flight.flightNumber:{" "}^10}   {flight.type:{" "}^12}   {flight.dest:{" "}^8}   {flight.price:{" "}^10}")
    if("i" == str(input("I(Igen) / N(Nem)")).lower()):
      self.tickets.pop(index)

  def view(self,AirMan:AirManager):
    print(f"{"Azonosító":{" "}^8} {"Neve":{" "}^20}  {"Járatszám":{" "}^10}   {"Típus":{" "}^12}   {"Uticél":{" "}^8}   {"Ár(Ft)":{" "}^10}")
    for i, ticket in enumerate(self.tickets):
      flight = AirMan.get_flight_by_number(ticket['flightNumber'])
      print(f"{i:{" "}^8} {ticket['name']:{" "}^20} {flight.flightNumber:{" "}^10}   {flight.type:{" "}^12}   {flight.dest:{" "}^8}   {flight.price:{" "}^10}")
