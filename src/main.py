''' Core / Main file or project '''

print("\n\t     Arithemic/Logical/Formula Calculation & Conversations \n")

print("\n\t      Press & Enter (A) - Arithematic Calculations \n")

print("\n\t     Press & Enter (C) - Conversion Calculations \n")

print("\n\t    Press & Enter (F) - formulas Calculations  \n")

print("\n\t      Press & Enter (CC) - Comparison Calculations \n")

print("\n\n - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

while True:

    ''' Take input from the user '''

    alphabet = input("\nFrom Above Statements - Provide a Number to Perform Operation \n\n\t\tPress - ( A - C - F - CC) : ")

    ''' Check if choice is one of the four options '''

    alphabet = alphabet.upper()

    if alphabet in ('A', 'C', 'F', 'CC'):

        if alphabet == 'A':

            from Arithematic_Calculations import *

        elif alphabet == 'C':

            from Conversion__Calculations import *

        elif alphabet == 'F':

            from Formulas_Calculations import *

        elif alphabet == 'CC':

            from Comparison_Calculations import *

        break

    else:
        print("\n\t\t\tInvalid Input")
