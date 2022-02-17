from turtle import clear
import MainM
import sys
import time
import os

#################
#Character points

#################
##################
#Text typing speed
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
def print_very_slow(str):
    for letter in str:              
        sys.stdout.write(letter)   
        sys.stdout.flush()         
        time.sleep(0.15)
def print_fast(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)           
##################
if MainM.answer == "y":
    print_fast("You wake up in a hospital bed.\n")
    print("     -You")
    print_slow("Where am I? What's going on?")
else:
    print("Okay see ya!")
    time.sleep(5)
    exit()

answer1 = input("""\n--What would you like to do now?
 1 - Go brew some tea.
 2 - Go to sleep

""")
if answer1 == "1":
    print_slow("You made some tea")
    time.sleep(10)
if answer1 == "2":
    print("You cried yourself to sleep, again.")
    time.sleep(10)