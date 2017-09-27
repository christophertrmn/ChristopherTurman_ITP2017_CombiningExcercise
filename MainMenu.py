
from Burger_Simulator_Segment import *
while True:
    print("Please input one of the commands!")
    command = input("1.Gladiator 2.Burger Simulator 3.Exit")
    if command == "1"or command.lower() == "gladiator":
        from Gladiator import *
        Mainmenu()
    elif command == "2" or command.lower() == "burger simulator":
        burger()
    elif command == "3" or command.lower() == exit:
        break
    else:
        print("Error")
