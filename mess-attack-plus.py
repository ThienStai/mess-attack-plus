from pyautogui import typewrite, FAILSAFE, press, MINIMUM_DURATION, FailSafeException
from time import sleep
from os import system
from sys import exit
from py
print("\nWelcome to MessAttack v1.0 by thien")
print("\nChoose a attack mode to begin:\n")
print("unsafe : type as fast as possible, may cause lag")
print("safe   : type with delay and fail-safe")
print("absafe : have even more delay options")
option = str(input("\nYour option: ")).lower()
MINIMUM_DURATION = 0.0001

def countdown():
    system("cls")
    print("\n\nMove your mouse to the Mess input box and click it!!!\n\n")
    sleep(2.5)
    system("cls")
    print("\nThanks for using MessAttack v1.0.0 by Thien.")
    print("Attack begin in 3.")
    sleep(1)
    print("Attack begin in 2.")
    sleep(1)
    print("Attack begin in 1.")
    sleep(1)
    system("cls")

def CheckZero(enter_delay, letter_delay):
    if enter_delay == 0 or letter_delay == 0:
        system("cls")
        print("Crash due to you typed zero")
        sleep(2)
        exit()

def quit():
    system("cls")
    print("\n\nInvalid option!!!")
    sleep(0.5)
    exit()

def invalid(times_to_spam, letter_delay):
    if (times_to_spam.isdecimal == False) or (letter_delay.isalnum == False):
        quit()   

def warning():
    system("cls")
    print("\n\n\nTHIS IS THE LAST WARNING!!")
    print("THIS APP MIGHT CAUSE YOUR PC TO FREEZE OR BSOD!!")
    print("SO BETTER USEING SAFEMODE!!")
    print("ARE YOU SURE YOU WANT TO CONTINUE?(y/n)")

try:
    ###----------------------UNSAFE GO HERE------------------------###
    ###----------------------UNSAFE GO HERE------------------------###
    ###----------------------UNSAFE GO HERE------------------------###

    if option == "unsafe":
        print("\nIf lag then move your mouse to upper left screen corner to exit!")
        FAILSAFE = True
        string_to_spam = str(input("\nWhat string do you want to use as a weapon?\n>>>"))
        times_to_spam = str(input("How many times do you want to spam it?\n>>>"))
        if times_to_spam.isdecimal == False:
            system("cls")
            print("Invalid option!!!")
            sleep(0.5)
            exit()
        warning()
        danger = str(input()).lower()
        if danger == "y":
            countdown()
            for i in range(0, int(times_to_spam)):
                typewrite(string_to_spam)
                press('enter')
                print("Spammed " + str(i) + " times, " + str(int(times_to_spam) - i) + " spams left")
            print("Done!\nThanks for using this app!")
        else:
            quit()

    ###----------------------SAFE GO HERE------------------------###
    ###----------------------SAFE GO HERE------------------------###
    ###----------------------SAFE GO HERE------------------------###

    elif option == "safe":
        print("\nIf lag then move your mouse to upper left screen corner to exit!")
        FAILSAFE = True
        string_to_spam = str(input("\nWhat string do you want to use as a weapon?\n>>>"))
        times_to_spam = str(input("How many times do you want to spam it?\n>>>"))
        enter_delay = float(input("Type the delay value after type and press enter:(>0.001 is nothing)\n>>>"))
        letter_delay = input("Type the delay value between each letter:(>0.001 is nothing)\n>>>")
        invalid(times_to_spam, letter_delay)
        sleep(0.5)
        CheckZero(enter_delay, letter_delay)
        countdown()
        for i in range(0, int(times_to_spam)):
            typewrite(string_to_spam, interval=float(letter_delay))
            sleep(enter_delay)
            press('enter')
            print("Spammed " + str(i) + " times, " + str(int(times_to_spam) - i) + " spams left")
        print("Done!\nThanks for using this app!")

    ###----------------------ABSAFE GO HERE------------------------###
    ###----------------------ABSAFE GO HERE------------------------###
    ###----------------------ABSAFE GO HERE------------------------###

    elif option == "absafe":
        print("\nIf laf then move your mouse to upper left screen corner to exit!")
        FAILSAFE = True
        string_to_spam = str(input("\nWhat string do you want to use as a weapon?\n>>>"))
        times_to_spam = str(input("How many times do you want to spam it?\n>>>"))
        enter_delay = float(input("Type the delay value after type and press enter:(>0.001 is nothing)\n>>>"))
        enter_delay2 = float(input("Type the delay value after press enter and type:(>0.001 is nothing)\n>>>"))
        letter_delay = input("Type the delay value between each letter:(>0.001 is nothing)\n>>>")
        invalid(times_to_spam, letter_delay)
        sleep(0.5)
        CheckZero(enter_delay, letter_delay)
        CheckZero(enter_delay2, letter_delay)
        countdown()
        for i in range(0, int(times_to_spam)):
            sleep(enter_delay2)
            typewrite(string_to_spam, interval=float(letter_delay))
            sleep(enter_delay)
            press('enter')
            print("Spammed " + str(i) + " times, " + str(int(times_to_spam) - i) + " spams left")
        print("Done!\nThanks for using this app!")

























    else:
        quit()
except FailSafeException:
    system("cls")
    print("MessAttack now exiting!")
    sleep(1)
    exit()
