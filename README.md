# Coin Calculator

## Introduction
This is the Coin Calculator, a small program that I was tasked with creating during my Fundamentals of Computing class at Jacksonville State University. This program takes the amount of each type of coin that the user has and outputs the value of those coins in both cents and dollars.

## Process
1. The program begins by asking the user to input the amount of pennies that they have. If they enter an amount that is lower than zero, the program informs them that they cannot have a negative amount of pennies and prompts them to try again. If they enter an amount of zero or greater, the amount is saved into the variable "**pennies**." The program then asks the same question for nickels (input saved to variable "**nickels**"), dimes (input saved to variable "**dimes**"), quarters (input saved to variable "**quarters**"), half dollars (input saved to variable "**halfdollars**"), and dollars (input saved to variable "**dollars**").
2. After recieving all of these inputs, the program prints each coin amount back onto the screen to assure the user that it has correctly recieved the data.
3. The program calculates the total value of the coins in cents and prints it to the screen. It calculates the total value using the following formula:
  >*value = pennies + (nickels * 5) + (dimes * 10) + (quarters * 25) + (halfdollars * 50) + (dollars * 100)*
4. After calculating the total in cents, the program calculates the monetary value of the coins (the value of the coins in dollars) and prints it to the screen. It calculates the monetary value by dividing the amount saved in "**value**" by 100.
5. After calculating both values, the user is prompted to press the **Enter** key to close the program.
