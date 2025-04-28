from flights.flight import Flight


class InterFlight(Flight):
    def __init__(self,flightNumber_Pref:str, dest:str, price:int):
      super().__init__(flightNumber_Pref, dest,price,"Belföldi")