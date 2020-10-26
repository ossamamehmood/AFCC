''' Formula's Calculations using Functions '''

print("\n\t     Formula's Calculations - Select Yours Operation")

print("\n\t           Press & Enter (A) - Average")

print("\n\t          Press & Enter (P) - Percentage")

print("\n\t      Press & Enter (MM) - Maximum & Minimum")

print("\n\t      Press & Enter (EO) - Even or Odd Number")

print("\n\t   Press & Enter (PC) - Prime or Consonant Number")

print("\n\t      Press & Enter (PN) - Positive or Negative")

print("\n\tPress & Enter (SCFF) - Square, Cube, Fourth & Fivthpower")

print("\n\t        Press & Enter (ATCS) - Area of Triangle, Cricle & Sphere")

print("\n\t    Press & Enter (SDT) - Speed, Distance & Time")

print("\n\n - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

while True:

    formulas = input("\nFrom Above Statements - Provide a Number to Perform Calculation \n\nPress - ( A - P - MM - EO - PC - PN - SCFF - ATCS - SDT ) : ")

    formulas = formulas.upper()

    if formulas in ('A','P','MM','EO','PC','PN','SCFF','ATCS','SDT'):

        if formulas == 'A':

            ''' Average '''

            num = int(input("\nProvide Number of Value's you want Calculate:"))

            def avg():

                sum = 0

                for i in range(num):

                    number = int(input("\nDecide a Number : "))

                    sum = sum + number

                    average = sum / num

                    print("\n\tThe Average of Numbers will be", round(average,2))

            avg()

        elif formulas == 'P':

            ''' Percentage '''

            num = int(input("\nProvide Number of Value's you want Calculate:"))

            def per():

                sum = 0

                for i in range(num):

                    number = eval(input("\nDecide a Number : "))

                    sum = sum + number

                percentage = sum / 100

                print("\n\tThe Percentage of Numbers will be", round(percentage,2))

            per()

        elif formulas == 'MM':

            ''' Maximum & Minimum '''

            my_list = []

            num = int(input("\nProvide Number of Value's you want Calculate:"))

            def display():

                for i in range(num):

                    numbers = int(input("\nDecide a Number : "))

                    my_list.append(numbers)

                print("\n\tMaximum element in the list is :", max(my_list), "\n\n\tMinimum element in the list is :", min(my_list))

            display()

        elif formulas == 'EO':

            ''' Even or Odd '''

            num = int(input("\nDecide a Number : "))

            def display(num):

                if (num % 2 == 0):

                    print("\n\t",num, "Is Even Number")

                else:
                    print("\n\t",num, "Is Odd Number")

            display(num)

        elif formulas == 'PC':

            ''' Prime & Consonant Numbers '''

            def prime(num):

                if num > 1:

                    for i in range(2, num):

                        if (num % i) == 0:

                            print(num, "is not a Prime Number - Consonant Number")

                            break

                    else:

                        print(num, "is a Prime Number - Not a Consonant Number")
                else:

                    print(num, "is not a Prime Number - Consonant Number")

                return ""

            number = int(input("\n\tProvide a Number to Check : "))

            print()

            print(prime(number))

        elif formulas == 'PN':

            ''' Positive or Negative '''

            num = eval(input("\nDecide a Number : "))

            def integer():

                if num > 0:

                    print("\n\t",num, "Is Positive Integer")

                elif num == 0:

                    print(" Integer Is Neither Positive & Nor Negative - (ZERO)")

                else:
                    print("\n\t",num, "Is Negative Integer")

            integer()

        elif formulas == 'SCFF':

            ''' Square, Cube, Fourthpower and Fifthpower '''

            def square(num):

                print("\n\tThe Square of Number will be ",num * num)

                return ""

            def cube(num):

                print("\n\tThe Cube of Number will be ",num * num * num)

                return ""

            def fourthpower(num):

                print("\n\tThe Fourth Power of Number will be ",num * num * num * num)

                return ""

            def fifthpower(num):

                print("\n\tThe Fifth Power of Number will be ",num * num * num * num * num)

                return ""

            ''' Function Calling / Execution - For Square, Cube, 4th & 5th Power '''

            print("\n\t Select Your Root to Perform. \n")

            print("\n\t     Press S - For Square \n")

            print("\n\t      Press C - For Cube \n")

            print("\n\t   Press FOU - For Fourth Power \n")

            print("\n\t   Press FIF - For Fifth Power \n\n")

            while True:

                ''' Take input from the user '''

                formulas = input("Enter Your choice For Root - Press - ( S - C - FOU - FIF) : ")

                formulas = formulas.upper()

                ''' Check if choice is one of the four options '''

                if formulas in ('S', 'C', 'FOU', 'FIF'):

                    num = int(input("\nDecide a number for the selected root: "))


                    if formulas == 'S':

                        print(square(num))

                    elif formulas == 'C':

                        print(cube(num))

                    elif formulas == 'FOU':

                        print(fourthpower(num))

                    elif formulas == 'FIF':

                        print(fifthpower(num))

                    break

                else:
                    print("Invalid Input")

        elif formulas == 'ATCS':

            ''' Area of Triangle, Circle & Sphere '''

            def areaoftriangle():

                height = h = int(input("\nDecide the Height of Triangle : "))

                base = b = int(input("\nDecide the Base of Triangle : "))

                areaoftriangle = (height * base) / 2

                print("\n\tArea of Triangle = ", round(areaoftriangle, 2))

                return ""

            def areaofcircle():

                pi = 3.14

                radius = r = int(input("\nDecide the Radius : "))

                areaofcircle = pi * ( radius ** 2 )

                print("\n\tArea of Triangle = ", round(areaofcircle, 2))

                return ""

            def areaofsphere():

                pi = 3.14

                radius = r = int(input("\nDecide the Radius : "))

                areaofsphere = 4 * pi * (r ** 2)

                print("\n\tArea of Sphere = ", round(areaofsphere,2))

                return ""

            print("\n\t Select Your Choice to Calculate Area of Triangle, Circle or Sphere \n")

            print("\n\t   Press & Enter (AT) - Area of Triangle \n")

            print("\n\t   Press & Enter (AC) - Area of Circle \n")

            print("\n\t   Press & Enter (AS) - Area of Sphere \n")

            while True:

                ''' Take input from the user '''

                formulas = input("Enter Your choice For Calculation - Press - ( AT - AC - AS ) : ")

                formulas = formulas.upper()

                ''' Check if choice to Calculate Speed, Time or Distance '''

                if formulas in ('AT', 'AC', 'AS'):

                    if formulas == 'AT':

                        print(areaoftriangle())

                    elif formulas == 'AC':

                        print(areaofcircle())

                    elif formulas == 'AS':

                        print(areaofsphere())

                    break

                else:

                    print("Invalid Input")

        elif formulas == 'SDT':

            ''' Speed, Distance & Time '''

            def speed(distance, time):

                distance = int(input("\nDecide the Distance (KM) - To Calculate Speed : "))

                time = int(input("\nDecide the Time (S) - To Calculate Speed : "))

                speed = distance * time

                return speed


            def distance(speed, time):

                speed = int(input("\nDecide the Speed (M/S) - To Calculate Distance : "))

                time = int(input("\nDecide the Time (S) - To Calculate Distance : "))

                distance = speed / time

                return distance

            def time(speed, distance):

                speed = int(input("\nDecide the Speed (M/S) - To Calculate Time : "))

                distance = int(input("\nDecide the Distance (KM)- To Calculate Time : "))

                time = speed / distance

                return time

            print("\n\t Select Your Choice to Calculate Speed, Time or Distance \n")

            print("\n\t   Press S - Speed (M/S) \n")

            print("\n\t   Press D - Distance (KM) \n")

            print("\n\t   Press T - Time (S) \n")

            while True:

                ''' Take input from the user '''

                formulas = input("Enter Your choice For Calculation - Press - ( S - D - T ) : ")

                ''' Check if choice to Calculate Speed, Time or Distance '''

                formulas = formulas.upper()

                if formulas in ('S', 'D', 'T'):

                    if formulas == 'S':

                        print("\n\tSpeed - According To - Given Distance & Time : ",speed(distance, time), end=' (Meter Per Second)')

                    elif formulas == 'D':

                        print("\n\tDistance - According To - Given Speed & Time : ",distance(speed, time), end=' (Kilometers)')

                    elif formulas == 'T':

                        print("\n\tTime - According To - Given Speed & Distance : ",time(speed, distance), end=' (Second)')

                    break

                else:

                    print("Invalid Input")

        break

    else:

        print("Invalid Input")