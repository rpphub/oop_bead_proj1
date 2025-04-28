from flights.inter_flight import InterFlight
from flights.dom_flight import domFlight
from airline.airline import Airline
from airline.manager import AirManager
from ticketing.ticketing import Tickets

def print_header():
  print(r"""
 /$$$$$$$  /$$$$$$$       /$$$$$$$$ /$$$$$$  /$$$$$$  /$$   /$$ /$$$$$$$$ /$$$$$$$$ /$$$$$$ /$$   /$$  /$$$$$$ 
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
          InterFlight("W4","BUD",35000),
          InterFlight("W4","DEB",20000),
          InterFlight("W4","SOB",20000)
        ),
          Airline(
          "Ryanair",
          InterFlight("FR","BUD",35000),
          InterFlight("FR","DEB",15000),
          InterFlight("FR","SOB",14000)
        ),
          Airline(
          "Turkish Airlines",
          domFlight("TK","IST",35000),
          domFlight("TK","SAW",45000),
          domFlight("TK","ISL",55000)
        )
    )
    #Statikus foglalások hozzáadás
    Ticketing = Tickets({
        "name": "Fá Zoltán",
        "flightNumber": "W41"
    },
    {
        "name": "Heu Réka",
        "flightNumber": "W41"
    },
    {
        "name": "Krump Lee",
        "flightNumber": "FR5"
    },
    {
        "name": "Nap Pali",
        "flightNumber": "TK7"
    },
    {
        "name": "Díz Elek",
        "flightNumber": "TK8"
    },
    {
        "name": "Har Mónika",
        "flightNumber": "W43"
    })

    print_header()
    while True:
      
      print()
      print("Válasszon a lehetőségek közül!")
      print("-------------------------------")
      print("1. Járatok listája")
      print("2. Járat Foglalás")
      print("3. Foglalás törlése")
      print("4. Foglalások listája")
      print("5. Kilépés")
      print("-------------------------------")
      print()
      
      try:
        choice = int(input("Válasszon egy opciót: "))
        if choice == 1:
            print("- Járatok listája -")
            print()
            AirMan.view_all_flight()
        elif choice == 2:
            print("- Járat Foglalás -")
            print()
            name = str(input("Adja meg a nevét: "))
            flightNumber = str(input("Adja meg a járat számát: ").upper())
            Ticketing.buy(AirMan, name, flightNumber)
        elif choice == 3:
            print("- Foglalás törlése -")
            print()
            ticketId = int(input("Adja meg a törlendő foglalás azonosítóját: "))
            Ticketing.cancel(AirMan, ticketId)
        elif choice == 4:
            print("- Foglalások listája -")
            print()
            Ticketing.view(AirMan)
        elif choice == 5:
            print("--------- Viszlát ! ----------")
            print()
            break
        else:
            print(f"\n Nincs ilyen menüpont({choice}).")

      except ValueError:
        print("\n Csak számot adhat meg.")

if __name__ == '__main__':
    main()