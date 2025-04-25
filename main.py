from flights.inter_flight import InterFlight
from flights.dom_flight import domFlight
from airline.airline import Airline
from airline.manager import AirManager
from ticketing.ticketing import Tickets

def print_header():
  print("""/$$$$$$$  /$$$$$$$       /$$$$$$$$ /$$$$$$  /$$$$$$  /$$   /$$ /$$$$$$$$ /$$$$$$$$ /$$$$$$ /$$   /$$  /$$$$$$ 
| $$__  $$| $$__  $$     |__  $$__/|_  $$_/ /$$__  $$| $$  /$$/| $$_____/|__  $$__/|_  $$_/| $$$ | $$ /$$__  $$
| $$  \ $$| $$  \ $$        | $$     | $$  | $$  \__/| $$ /$$/ | $$         | $$     | $$  | $$$$| $$| $$  \__/
| $$$$$$$/| $$$$$$$/ /$$$$$$| $$     | $$  | $$      | $$$$$/  | $$$$$      | $$     | $$  | $$ $$ $$| $$ /$$$$
| $$____/ | $$__  $$|______/| $$     | $$  | $$      | $$  $$  | $$__/      | $$     | $$  | $$  $$$$| $$|_  $$
| $$      | $$  \ $$        | $$     | $$  | $$    $$| $$\  $$ | $$         | $$     | $$  | $$\  $$$| $$  \ $$
| $$      | $$  | $$        | $$    /$$$$$$|  $$$$$$/| $$ \  $$| $$$$$$$$   | $$    /$$$$$$| $$ \  $$|  $$$$$$/
|__/      |__/  |__/        |__/   |______/ \______/ |__/  \__/|________/   |__/   |______/|__/  \__/ \______/""")
  print()



def main():


    AirMan = AirManager(
          Airline(
          "Wizz air",
          InterFlight("BUD",35000),
          InterFlight("DEB",20000),
          InterFlight("SOB",20000)
        ),
          Airline(
          "Ryanair",
          InterFlight("BUD",35000),
          InterFlight("DEB",15000),
          InterFlight("SOB",14000)
        ),
          Airline(
          "Turkish Airlines",
          domFlight("IST",35000),
          domFlight("SAW",45000),
          domFlight("ISL",55000)
        )
    )

    AirMan.add_airline(
            Airline(
            "Teszt",
            domFlight("IST",35000),
            domFlight("ISL",55000)
            )
        )
    print_header()
    print("Válasszon a lehetőségek közül!")
    print("-------------------------------")
    print("1. Járatok listája")
    print("2. Járat Foglalás")
    print("3. Foglalás törlése")
    print("4. Foglalások listája")
    print("-------------------------------")

    AirMan.view_all_flight()
    Ticketing = Tickets()
    Ticketing.buy(8)
    Ticketing.buy(4)
    Ticketing.view(AirMan)

if __name__ == '__main__':
    main()