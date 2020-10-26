''' Conversions Calculations using Functions '''

print("\n\t       Conversions Calculations - Select Yours Operation \n")

print("\n\t     Press & Enter (CI) - Centimeters to Inches & Vice Versa")

print("\n\t     Press & Enter (IM) - Inches to Meters & Vice Versa")

print("\n\t     Press & Enter (FI) - Foot to Inches & Vice Versa")

print("\n\t     Press & Enter (KM) - Kilometers to Meters & Vice Versa")

print("\n\t     Press & Enter (CF) - Celsius into Fahrenheit & Vice Versa")



print("\n\n - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

while True:

    conversion = input("\nFrom Above Statements - Provide a Number to Perform Calculation : \n\n\t\tPress - ( CI - IM - FI - KM - CF ) : ")

    conversion = conversion.upper()

    if conversion in ('CI','IM','FI','KM','CF'):

        if conversion == 'CI':

            ''' Centimeter into inches '''

            def inches(num):

                ''' Converting from Centimeters to inches '''

                ''' 1 Inch = 2.54 Centimeters '''

                inches = num * 2.54

                return inches

            def centimeters(num):

                ''' Converting from inches to cms '''

                '''  2.54 Centimeters = 1 Inch '''

                centimeters = num / 2.54

                return centimeters

            print("\n\t    Choose - Centimeters to Inches - Vice Versa")

            print("\n\t     Press & Enter (C) - Centimeters to Inches")

            print("\n\t     Press & Enter (I) - Inches to Centimeters")

            print("\n - - - - - - - - - - - - - - - - - - - - - - - - - ")

            while True:

                conversion = input("\nFrom Above Statements - Provide a Number to Perform Operation : \n\n\t\tPress - ( C - I ) : ")

                conversion = conversion.upper()

                if conversion in ('C','I'):

                    if conversion == 'C':

                        num = float(input("\nDistance measured in Centimeter : "))

                        print("\n\tDistance in inch : ",round(inches(num),2), end=' (Centimeters)')

                    elif conversion == 'I':

                        num1 = float(input("\nDistance measured in Inches : "))

                        print("\n\tDistance in Centimeters : ", round(centimeters(num1),2), end=' (Inches)')

                    break

                else:
                    print("\n\tInvalid Operator")

        elif conversion == 'IM':

            ''' Inches into meters '''

            def inches(length):

                ''' Converting from inches to meters '''

                ''' 1 Inch = 0.0254 Meters '''

                inches = length / 39.3701

                return inches


            def meters(length):

                ''' Converting from meters to inches '''

                '''  1 Meters = 39.3701 Inches '''

                meters = length * 0.0254

                return meters


            print("\n\t    Choose - Inches to Meters - Vice Versa")

            print("\n\t     Press & Enter (I) - Inches to Meters")

            print("\n\t     Press & Enter (M) - Meters to Inches")

            print("\n - - - - - - - - - - - - - - - - - - - - - - - - - ")

            while True:

                conversion = input("\nFrom Above Statements - Provide a Number to Perform Operation : \n\n\t\tPress - ( I - M ) : ")

                conversion = conversion.upper()

                if conversion in ('I','M'):

                    if conversion == 'I':

                        num = float(input("\nDistance measured in meters : "))

                        print("\n\tDistance in inch : ",round(inches(num),2), end=' (mm)')

                    elif conversion == 'M':

                        num = float(input("\nDistance measured in inches : "))

                        print("\n\tDistance in meters : ", round(meters(num),2), end=' (m)')

                    break

                else:

                    print("\n\tInvalid Operator")

        elif conversion == 'FI':

            ''' Foot into Inches '''

            def foot(length):

                ''' Converting from foot to inches '''

                ''' 1 kilometer = 1000 Meters '''

                foot = length * 12

                return foot


            def inches(length):

                ''' Converting from inches to foot '''

                ''' 1000 meters = 1 Kilometer '''

                inches = length / 12

                return inches


            print("\n\t    Choose - Foot to Inches - Vice Versa")

            print("\n\t     Press & Enter (F) - Foot to Inches")

            print("\n\t     Press & Enter (I) - Inches to Inches")

            print("\n - - - - - - - - - - - - - - - - - - - - - - - - - ")

            while True:

                conversion = input("\nFrom Above Statements - Provide a Number to Perform Operation : \n\n\t\tPress - ( F - I ) : ")

                conversion = conversion.upper()

                if conversion in ('F', 'I'):

                    if conversion == 'F':

                        num = float(input("\nDistance measured in foot : "))

                        print("\n\tDistance in Inches : ", round(foot(num), 2), end=' (inches)')

                    elif conversion == 'I':

                        num = float(input("\nDistance measured in inches : "))

                        print("\n\tDistance in foot : ", round(inches(num), 2), end=' (foot)')

                    break

                else:

                    print("\n\tInvalid Operator")

        elif conversion == 'KM':

            ''' Kilometers into meters '''

            def kilometers(length):

                ''' Converting from inches to meters '''

                ''' 1 kilometer = 1000 Meters '''

                kilometers = length * 1000

                return kilometers


            def meters(length):

                ''' Converting from inches to meters '''

                ''' 1000 meters = 1 Kilometer '''

                meters = length / 1000

                return meters


            print("\n\t    Choose - Kilometers to Meters - Vice Versa")

            print("\n\t     Press & Enter (K) - Kilometers to Meters")

            print("\n\t     Press & Enter (M) - Meters to Kilometers")

            print("\n - - - - - - - - - - - - - - - - - - - - - - - - - ")

            while True:

                conversion = input("\nFrom Above Statements - Provide a Number to Perform Operation : \n\n\t\tPress - ( K - M ) : ")

                conversion = conversion.upper()

                if conversion in ('K', 'M'):

                    if conversion == 'K':

                        num = float(input("\nDistance measured in meters : "))

                        print("\n\tDistance in Kilometers : ", round(kilometers(num), 2), end=' (kilometers)')

                    elif conversion == 'M':

                        num = float(input("\nDistance measured in kilometers : "))

                        print("\n\tDistance in meters : ", round(meters(num), 2), end=' (meters)')

                    break

                else:

                    print("\n\tInvalid Operator")


        elif conversion == 'CF':

            ''' Celsius into Fahrenheit '''

            ''' Formula : T(°F) = T(°C) × 9/5 + 32
                         
                                OR
                             
            Formula : Temp. in Fahrenheit = Temp. in Celsius × 9/5 + 32 '''


            def fahrenheit():

                celsius = float(input("\n\t\t    Temperature in Celsius: "))

                ''' Using above Formula '''

                fahrenheit = (celsius * (9 / 5)) + 32

                print("\n\t\t    Temp. in Fahrenheit from Celsius")

                print("\n\t\t     Temperature in Fahrenheit: ", round(fahrenheit))

                return ""


            ''' Formula : T(°C) = T(°F) - 32 × 9/5
sdsd
                                 OR

            Formula : Temp. in Celsius = Temp. in Fahrenheit - 32 × 9/5 '''

            def celsius():

                fahrenheit = float(input("\n\t\t    Temperature in Fahrenheit: "))

                ''' Using above Formula '''

                celsius = (fahrenheit - 32) * 5 / 9

                print("\n\t\t    Temp. in Fahrenheit from Celsius")

                print("\n\t\t     Temperature in Celsius: ", round(celsius))

                return ""

            print("\n\t    Choose - Celsius to Fahrenheit - Vice Versa")

            print("\n\t     Press & Enter (C) - Celsius to Fahrenheit ")

            print("\n\t     Press & Enter (F) - Fahrenheit to Celsius")

            print("\n - - - - - - - - - - - - - - - - - - - - - - - - - ")

            while True:

                conversion = input("\nFrom Above Statements - Provide a Number to Perform Operation : \n\n\t\tPress - ( C - F ) : ")

                conversion = conversion.upper()

                if conversion in ('C', 'F'):

                    if conversion == 'C':

                        print(fahrenheit())

                    elif conversion == 'F':

                        print(celsius())
                    break

                else:

                    print("\n\tInvalid Operator")

    break

else:

    print("Invalid Input")