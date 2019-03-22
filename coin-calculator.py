#  --------------------------------------------Getting the Coin Amounts-------------------------------------------- #
pennies = int(input("How many pennies do you have?  "))
while pennies < 0:
    pennies = int(input("You cannot have a negative amount of pennies! Please enter an amount of at least 0.   "))

nickels = int(input("How many nickels do you have?  "))
while nickels < 0:
    nickels = int(input("You cannot have a negative amount of nickels! Please enter an amount of at least 0.   "))

dimes = int(input("How many dimes do you have?  "))
while dimes < 0:
    dimes = int(input("You cannot have a negative amount of dimes! Please enter an amount of at least 0.   "))

quarters = int(input("How many quarters do you have?  "))
while quarters < 0:
    quarters = int(input("You cannot have a negative amount of quarters! Please enter an amount of at least 0.   "))

halfdollars = int(input("How many half dollars do you have?  "))
while halfdollars < 0:
    halfdollars = int(input("You cannot have a negative amount of half dollars! Please enter an amount of at least 0.   "))

dollars = int(input("How many dollars do you have?  "))
while dollars < 0:
    dollars = int(input("You cannot have a negative amount of dollars! Please enter an amount of at least 0.   "))

print("")
# ----------------------------------------------------------------------------------------------------------------- #


#  ----------Printing the Coin Amounts---------- #
print("You have", pennies, "pennies.")
print("You have", nickels, "nickels.")
print("You have", dimes, "dimes.")
print("You have", quarters, "quarters.")
print("You have", halfdollars, "half dollars.")
print("You have", dollars, "dollars.")
print("")
# ---------------------------------------------- #


#  -----------------------------------Calculating the Value in Cents----------------------------------- #
value = pennies + (nickels * 5) + (dimes * 10) + (quarters * 25) + (halfdollars * 50) + (dollars * 100)

print("The value of all of your coins is:", value, "cents.")
# ----------------------------------------------------------------------------------------------------- #


#  ---------------Calculating the Monetary Value--------------- #
moneyvalue = value/100
print("The monetary value of your coins is: $", moneyvalue, ".")
# ------------------------------------------------------------- #


# --------------Closing-------------- #
print("")
print("Press the ENTER key to close.")
input()
# ----------------------------------- #


#  Program Made by Logan Finley
