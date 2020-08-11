import sys
import keyboard
from colorama import Fore, init

init(autoreset = True)

def addition():
    try:
        firstnumber = int(input(Fore.GREEN + "Enter the First Number: "))
        secondnumber = int(input(Fore.GREEN + "Enter the Second Number: "))
        print("")
        result = firstnumber + secondnumber
    except ValueError:
        print(Fore.RED + "Oops!")
        print(Fore.RED + "We cand Add Number and String")
        print(Fore.RED + "Try Again")
        addition()
    else:
        print(Fore.CYAN + "Addition of "+Fore.GREEN+str(firstnumber)+Fore.CYAN+" and "+Fore.GREEN+str(secondnumber)+Fore.CYAN+" is "+Fore.BLUE+str(result))
        print(Fore.RED+"EXECUTION COMPLETED")
        print("")
        choose_option()

def subraction():
    try:
        firstnumber = int(input(Fore.GREEN+"Enter the First Number: "))
        secondnumber = int(input(Fore.GREEN+"Enter the Second Number: "))
        print("")
        result = firstnumber - secondnumber
    except ValueError:
        print(Fore.RED+"Oops!")
        print(Fore.RED+"We Cant Subract Number and String")
        subraction()
    else:
        print(Fore.CYAN + "Subration of "+Fore.GREEN+str(firstnumber)+Fore.CYAN+" and "+Fore.GREEN+str(secondnumber)+Fore.CYAN+" is "+Fore.BLUE+str(result))
        print(Fore.RED+"EXECUTION COMPLETED")
        print("")
        choose_option()

def multiplication():
    try:
        firstnumber = int(input(Fore.GREEN+"Enter the First Number: "))
        secondnumber = int(input(Fore.GREEN+"Enter the Second Number: "))
        print("")
        result = firstnumber * secondnumber
    except ValueError:
        print(Fore.RED+"Oops!")
        print(Fore.RED+"We can't Multiply Number and String")
        print(Fore.RED+"Try Again")
        multiplication()
    else:
        print(Fore.CYAN + "Multiplicatuon of "+Fore.GREEN+str(firstnumber)+Fore.CYAN+" and "+Fore.GREEN+str(secondnumber)+Fore.CYAN+" is "+Fore.BLUE+str(result))
        print(Fore.RED+"ECECUTION COMPLETED")
        print("")
        choose_option()

def division():
    try:
        firstnumber = int(input(Fore.GREEN+"Enter the First Number: "))
        secondnumber = int(input(Fore.GREEN+"Enter the Second Number: "))
        print("")
        result = firstnumber / secondnumber
    except ValueError:
        print(Fore.RED+"Oops!")
        print(Fore.RED+"We can't Divide Number and String")
        print(Fore.RED+"Try Again")
        division()
    except ZeroDivisionError:
        print(Fore.RED+"Oops!")
        print(Fore.RED+"We cant divide a number by zero")
        division()
    else:
        print(Fore.CYAN + "Division of "+Fore.GREEN+str(firstnumber)+Fore.CYAN+" and "+Fore.GREEN+str(secondnumber)+Fore.CYAN+" is "+Fore.BLUE+str(result))
        print(Fore.RED+"EXECUTION COMPLETED")
        print("")
        choose_option()

def choose_option():
    print(Fore.YELLOW+"1.ADDITION\n2.SUBRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.Exit")
    try:
        case = int(input(">>>"))
        print("")
    except ValueError:
        print(Fore.RED+"Oops!")
        print(Fore.RED+"You had entered a incorect value")
        print(Fore.RED+"Try Again!")
        choose_option()
    else:
        if case == 1:
            print(Fore.BLUE+"ADDITION")
            addition()
        elif case == 2:
            print(Fore.BLUE+"SUBRACTION")
            subraction()
        elif case ==3:
            print(Fore.BLUE+"MULTIPLICATION")
            multiplication()
        elif case == 4:
            print(Fore.BLUE+"DIVISION")
            division()
        elif case == 5:
            print(Fore.RED+"Thanks For Using Me")
            print("")
            sys.exit(1)
        else:
            print(Fore.RED+"Oops!")
            print(Fore.RED+"Select Correct Option")
            choose_option()

def author():
    print(Fore.GREEN+("Script by ")+Fore.RED+("TITAN彡HACKY"))


author()
choose_option()
