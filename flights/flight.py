from abc import ABC, abstractmethod

class Flight(ABC):
    flightNumber = 0

    def __init__(self, dest: str, price: int, type: str):
        self.dest = dest
        self.price = price
        self.type = type

        #   Járatszámok egyediek.
        Flight.flightNumber += 1
        self.flightNumber = Flight.flightNumber

    def __str__(self):
        return f"{self.flightNumber} | {self.type} | {self.dest} | {self.price}"