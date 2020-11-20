from pyautogui import alert, typewrite, FAILSAFE, press, MINIMUM_DURATION, FailSafeException
from time import sleep
from os import system
from pyinputplus import inputInt, inputFloat

MINIMUM_DURATION = 0.0001


def countdown():
    for i in range(3):
        print("Attack start in %s " % (3-i)) 
        sleep(1)


def main():
    global FAILSAFE, FailSafeException, MINIMUM_DURATION
    Running = True
    while Running:
        system("cls")
        try:
            # ----------------------UNSAFE GO HERE------------------------
            print("\nWelcome to mess-attack-plus by thien")
            print("\nChoose a attack mode to begin:\n")
            print("unsafe : type as fast as possible, may cause lag")
            print("safe   : type with delay and fail-safe")
            option = input("\nYour option: ").lower()
            if option.lower() == "unsafe":
                print("\nIf lag then move your mouse to upper left screen corner to exit!")
                FAILSAFE = True
                string_to_spam = input("String to spam = ")
                times_to_spam = inputInt("Time to spam = ", min=1, max=2147483647)
                countdown()
                for i in range(0, int(times_to_spam)):
                    typewrite(string_to_spam)
                    press('enter')
                    print("Spammed %s times, %s spams left" % (i, times_to_spam - i))
                print("Done!\nThanks for using this app!")
                sleep(1)

            # ----------------------SAFE GO HERE------------------------
            elif option.lower() == "exit":
                exit(0)
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
                    print("Spammed %s times, %s spams left" % (i, times_to_spam - i))
                print("Done!\nThanks for using this app!")
                sleep(1)
            else:
                print("Invalid mode!!")
                sleep(1)
                continue
        except FailSafeException:
                alert(text="You canceled the attack!", title="Stopped")
                Running = False


try:
    if __name__ == '__main__':
        main()
except KeyboardInterrupt:
    print("Exiting...")
    sleep(1)
