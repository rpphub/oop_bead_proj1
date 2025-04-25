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

    #Statikus járatok hozzáadása
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
    #Statikus foglalások hozzáadás
    Ticketing = Tickets()

    print_header()
    while True:

      print("Válasszon a lehetőségek közül!")
      print("-------------------------------")
      print("1. Járatok listája")
      print("2. Járat Foglalás")
      print("3. Foglalás törlése")
      print("4. Foglalások listája")
      print("-------------------------------")
      print()
      
      try:
        choice = int(input("Válasszon egy opciót: "))
        if choice == 1:
            AirMan.view_all_flight()
        elif choice == 2:
            flightNumber = int(input("Adja meg a járat számát: "))
            Ticketing.buy(flightNumber)

        elif choice == 4:
            Ticketing.view(AirMan)
        else:
            print(f"\n Nincs ilyen menüpont({choice}).")

      except ValueError:
        print("\n Csak számot adhat meg.")

if __name__ == '__main__':
    main()