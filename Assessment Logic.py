"""
Create a program that helps someone create a budget. It should ask the user for
monthly income and the following expenses:
-Housing
-Food
-Transportation
-Phone
-Utilities
-Clothing

The program should get input from the user and convert each of the inputs to floats.
The program should tell the user how much money they have left after they have
paid all of their bills.
The program should calculate and display the income percentage of each budget item.
"""

monthly_income = int(input("What is your total monthly income? "))
housing = int(input("How much do you spend on housing each month? "))
food = int(input("How much do you spend on food each month? "))
transportation = int(input("How much do you spend on transportation each month? "))
phone = int(input("How much do you spend on your phone bill each month? "))
utilities = int(input("How much do you spend on your utilities each month? "))
clothing = int(input("How much do you spend on clothing each month? "))

print('Housing takes up ', format(monthly_income / housing, '.2f'), '% of your monthly budget')
print('Food takes up ', format(monthly_income / food, '.2f'), '% of your monthly budget')
print("Transportation takes up " + format(monthly_income / transportation, '.2f') + "% of your monthly budget")
print("Phone takes up " + format(monthly_income / phone, '.2f') + "% of your monthly budget")
print("Utilities takes up " + format(monthly_income / utilities, '.2f') + "% of your monthly budget")
print("Clothing takes up " + format(monthly_income / clothing, '.2f') + "% of your monthly budget")
