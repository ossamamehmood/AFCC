''' Comparison operators Calculation using Functions '''

print("\n\t Comparison Calculation - Select Yours Operation")

print("\n\t     Press & Enter (GT) - Greater Than")

print("\n\t     Press & Enter (LT) - Less Than")

print("\n\t     Press & Enter (EE) - Both are Equal or Unequal")

print("\n\t     Press & Enter (GE) - Greater Than Equal To")

print("\n\t     Press & Enter (LE) - Less Than Equal To")

print("\n\n - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

while True:

    comparison = input("\nFrom Above Statements - Provide a Number to Perform Calculation : \n\n\t\tPress - ( GT - LT - EE - GE - LE ) : ")

    comparison = comparison.upper()

    if comparison in ('GT','LT','EE','GE','LE'):

        if comparison == 'GT':

            ''' Greater Than '''

            def greater():

                ''' Comparison of Greater Than '''

                x = float(input("\n\t\t           Decide a Number : "))

                y = float(input("\n\t\t        Decide Another Number : "))

                if x > y:

                    print("\n\t\tThe value of", x, "is greater than", y)

                else:

                    print("\n\t\tThe value of", x, "isn't greater than", y)

                return x > y

            greater()

        elif comparison == 'LT':

            ''' Less Than '''

            def less():

                ''' Comparison of Less Than '''

                x = float(input("\n\t\t           Decide a Number : "))

                y = float(input("\n\t\t        Decide Another Number : "))

                if x < y:

                    print("\n\t\tThe value of", x, "is less than", y)

                else:

                    print("\n\t\tThe value of", x, "isn't less than", y)

                return x < y

            less()

        elif comparison == 'EE':

            ''' Less Than '''

            def equal():

                ''' Comparison of Equal & Unequal '''

                x = float(input("\n\t\t           Decide a Number : "))

                y = float(input("\n\t\t        Decide Another Number : "))

                if x == y:

                    print("\n\t\tThe value of",x,"is equal to",y)

                else:

                    print("\n\t\tThe value of",x,"isn't equal or unequal to",y)

                return x < y

            equal()

        elif comparison == 'GE':

            ''' Greater Than Equal To '''

            def greaterequal():

                ''' Comparison of Greater than Equal too '''

                x = float(input("\n\t\t           Decide a Number : "))

                y = float(input("\n\t\t        Decide Another Number : "))

                if x >= y:

                    print("\n\t\tThe value of",x,"is Greater Than equal to",y)

                else:

                    print("\n\t\tThe value of",x,"isn't Greater Than equal or unequal to",y)

                return x >= y

            greaterequal()


        elif comparison == 'LE':

            ''' Less Than Equal To '''

            def lessequal():

                ''' Comparison of Less than Equal too '''

                x = float(input("\n\t\t           Decide a Number : "))

                y = float(input("\n\t\t        Decide Another Number : "))

                if x <= y:

                    print("\n\t\tThe value of",x,"is Less Than equal to",y)

                else:

                    print("\n\t\tThe value of",x,"isn't Less Than equal or unequal to",y)

                return x <= y

            lessequal()

        break

    else:

        print("\n\t\t\t\t\tInvalid Input")