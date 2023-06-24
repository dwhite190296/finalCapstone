# This is a python program determining the amount someone will make on an investment or owe on a bond using if/else statements.
# The user selects either investment or bond and it will ask for further inputs to complete the calculation on what they will owe or make.
# It will output the amount the user will make or owe depending on investment or bond, term length, interest rate  and amount invested/owed.

import math
# Inputs:
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calcutlate the amount you'll have to pay on a home loan")

user_selection = input("Enter either 'investment' or 'bond' from the menu above to proceed: \n")
user_selection = user_selection.lower()

# Printing an error message if the user doesn't input one of the options
if user_selection != 'investment' and user_selection != 'bond':
    print('Please try again and make sure you input either investment or bond')

# Investments inputs:
if user_selection == 'investment':
    P = float(input('Please enter the amount being deposited: £'))
    r = float(input('Please enter the interest rate (do not inclue the percentage symbol): '))
    r = r / 100
    t = int(input('Please enter the number of years of the investment: '))
    interest = input("Please enter if the interst is 'simple' or 'compound': \n")
    interest = interest.lower() 
    # Investments outputs:
    if interest == 'simple':
        A = P*(1 + r*t)
        print('The total simple interest is: £' + str(A))
    else:
        A = P * math.pow((1+r),t)
        print('The total compound interest is: £' + str(A))

# Bonds inputs:
else:
    P = float(input('Please enter the value of the house: £ '))
    i = float(input('Please enter the annual interest rate(do not include the percentage symbol): '))
    i = (i / 100) / 12
    n = int(input('How long is the repayment term in months? '))
    # Bonds outputs:
    repayment = (i * P)/(1 - (1 + i)**(-n))
    print('The repayment total each month will be: £' + str(repayment))
