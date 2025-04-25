from flights.flight import Flight


class InterFlight(Flight):
    def __init__(self, dest:str, price:int):
      super().__init__(dest,price,"Belföldi")