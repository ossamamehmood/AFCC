''' Arithematic Calculations using Functions '''

def sum(n):

    sum = 0

    for num in range(n):

        number = int(input("\nProvide the Number to Calculate: "))

        sum = sum + number

    return sum

def sub(n):

    sub = 0

    for num in range(n):

        number = int(input("\nProvide the Number to Calculate: "))

        sub = sub - number

    return sub

def mul(n):

    mul = 1

    for num in range(n):

        number = int(input("\nProvide the Number to Calculate: "))

        mul = mul * number

    return mul

def div(num,num1):

    if num1 >= 1:

        return num / num1


''' Program Execution / Function Calling '''


print("\n\t     Arithematic Calculations - Select Yours Operation \n")

print("\n\t      Press & Enter (A) - Addition of Numbers \n")

print("\n\t     Press & Enter (S) - Subtraction of Numbers \n")

print("\n\t    Press & Enter (M) - Multiplication of Numbers \n")

print("\n\t      Press & Enter (D) - Division of Numbers ")

print("\n\n - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

while True:

    ''' Take input from the user '''

    arithematic = input("\nFrom Above Statements - Provide a Number to Perform Operation \n\n\t\tPress - ( A - S - M - D) : ")

    ''' Check if choice is one of the four options '''

    arithematic = arithematic.upper()

    if arithematic in ('A', 'S', 'M', 'D'):

        if arithematic == 'A':

            num = int(input("\nProvide Number of Value's you want Calculate: "))

            print("\n\tThe Addition of Numbers will be", sum(num))

        elif arithematic == 'S':

            num = int(input("\nProvide Number of Value's you want Calculate: "))

            print("\n\tThe Subtraction of Numbers will be", sub(num))

        elif arithematic == 'M':

            num = int(input("\nProvide Number of Value's you want Calculate: "))

            print("\n\tThe Multiplication of Numbers will be", mul(num))

        elif arithematic == 'D':

            num = eval(input("\n\t\t  Decide a number :  "))

            num1 = eval(input("\n\t\tDecide Another number :  "))

            print("\n\tThe Division of Numbers will be", round(div(num,num1),2))

        break

    else:
        print("\n\t\t\tInvalid Input")