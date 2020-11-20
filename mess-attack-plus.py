from pyautogui import typewrite, FAILSAFE, press, MINIMUM_DURATION, FailSafeException
from time import sleep
from os import system
from sys import exit
from pyinputplus import inputInt, inputFloat
print("\nWelcome to MessAttack v1.0 by thien")
print("\nChoose a attack mode to begin:\n")
print("unsafe : type as fast as possible, may cause lag")
print("safe   : type with delay and fail-safe")
print("absafe : have even more delay options")
option = str(input("\nYour option: ")).lower()
MINIMUM_DURATION = 0.0001


def countdown():
    for i in range(3):
        print("Attack start in %s ") % i
        sleep(1)
def main():
    global FAILSAFE, FailSafeException, MINIMUM_DURATION
    try:
        ###----------------------UNSAFE GO HERE------------------------###
        ###----------------------UNSAFE GO HERE------------------------###
        ###----------------------UNSAFE GO HERE------------------------###

        if option.lower() == "unsafe":
            print("\nIf lag then move your mouse to upper left screen corner to exit!")
            FAILSAFE = True
            string_to_spam = input("String to spam = ")
            times_to_spam = inputInt("Time to spam = ", min=1, max=2147483647)
            # countdown()
            for i in range(0, int(times_to_spam)):
                typewrite(string_to_spam)
                press('enter')
                print("Spammed %s times, %s spams left") % (i, times_to_spam-i)
            print("Done!\nThanks for using this app!")

        ###----------------------SAFE GO HERE------------------------###
        ###----------------------SAFE GO HERE------------------------###
        ###----------------------SAFE GO HERE------------------------###

        elif option == "safe":
            print("\nIf lag then move your mouse to upper left screen corner to exit!")
            FAILSAFE = True
            string_to_spam = input("String to spam = ")
            times_to_spam = inputInt("Time to spam = ", min=1, max=2147483647)
            enter_delay = inputFloat("Delay between typing string and press enter = ", min=0.002, max=2147483647)
            letter_delay = inputFloat("Delay between each letters = ", min=0.002, max=2147483647)
            countdown()
            for i in range(0, int(times_to_spam)):
                typewrite(string_to_spam, interval=letter_delay)
                sleep(enter_delay)
                press('enter')
                print("Spammed %s times, %s spams left" % (i, times_to_spam-i))
            print("Done!\nThanks for using this app!")

        ###----------------------ABSAFE GO HERE------------------------###
        ###----------------------ABSAFE GO HERE------------------------###
        ###----------------------ABSAFE GO HERE------------------------###

        elif option == "absafe":
            print("\nIf laf then move your mouse to upper left screen corner to exit!")
            FAILSAFE = True
            string_to_spam = input("String to spam = ")
            times_to_spam = inputInt("Time to spam = ", min=1, max=2147483647)
            enter_delay = inputFloat("Delay between typing string and press enter = ", min=0.002, max=2147483647)
            letter_delay = inputFloat("Delay between each letters = ", min=0.002, max=2147483647)
            countdown()
            for i in range(0, int(times_to_spam)):
                sleep(enter_delay2)
                typewrite(string_to_spam, interval=float(letter_delay))
                sleep(enter_delay)
                press('enter')
                print("Spammed %s times, %s spams left" % (i, times_to_spam-i))
            print("Done!\nThanks for using this app!")
    except FailSafeException:
        print("You canceled the operation!")

if __name__ == '__main__':
   main()
























    else:
        quit()
except FailSafeException:
    system("cls")
    print("MessAttack now exiting!")
    sleep(1)
    exit()
