# Imports required packages
import math

# Gets first number from user
x = int(input("Enter a number. "))

# Asks the user if they want to square this number
square = str(input("Square this number? "))

if square == "yes":
   print(x ** 2) # Squares the number 
   quit() # Quits the program
elif square == "no":

# Asks the user if they want to square root the number
   sqaureroot = str(input("How about square root? "))
else:
   print("Invalid try again.")
   quit()
if sqaureroot == "yes":
   print(math.sqrt(x)) # Square roots the number 
   quit()
elif sqaureroot == "no":
    y = int(input("Enter another number. ")) # Asks the user to input another number
else: 
   print("Invalid try again. ")
   quit()

# Asks the user to input an operation    
operation = str(input("Enter a operation e.g Addition or Subtraction. Enter factorise to factorise number 1 "))

if operation == "addition":
   print(x + y) # Adds the two numbers
elif operation == "subtraction":
   print(x - y) # Subtracts the two numbers
elif operation == "multiplication":
   print(x * y) # Multiplies the two numbers
elif operation == "division":
   print(x / y) # Divides the two numbers 
elif operation == "factorise":
   print(math.factorial(x)) # Factorises the first number (x)
else:
   print("Invalid operation! ") # If user inputs an invalid operation
