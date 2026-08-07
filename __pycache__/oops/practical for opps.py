# #I Ask the user for a number and print its square.• Handle ValueError if the user types text instead of a number.
# try:
#     num = int(input("Enter a number: "))
#     print("Square:", num ** 2)
# except ValueError:
#     print("Please enter a valid number.")
# #2 Create a program that divides two numbers entered by the user.Handle both ZeroDivisionError and ValueError.
# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     print("Result:", num1 / num2)
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# except ValueError:
#     print("Please enter valid numbers.")

# #Write a program that opens a file named "data.txt" and prints its contents. If the file does't exist, show "File not found!".
# try:
#     with open("data.txt", "r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File not found!")
# #4 Ask the user to enter their age.If they enter a negative number, raise a ValueError with message "Age cannot be negative!".
# try:
#     age = int(input("Enter your age: "))

#     if age < 0:
#         raise ValueError("Age cannot be negative!")

#     print("Your age is", age)

# except ValueError as age:
#     print(age)
# #Create a calculator that supports +, - *, /Use try-except to handle invalid operators or division by zero. Cl
# try:
#     num1 = float(input("Enter first number: "))
#     operator = input("Enter operator (+,-,*,/): ")
#     num2 = float(input("Enter second number: "))

#     if operator == "+":
#         print("Result:", num1 + num2)

#     elif operator == "-":
#         print("Result:", num1 - num2)

#     elif operator == "*":
#         print("Result:", num1 * num2)

#     elif operator == "/":
#         print("Result:", num1 / num2)

#     else:
#         raise ValueError("Invalid operator!")

# except ZeroDivisionError:
#     print("Cannot divide by zero.")

# except ValueError as e:
#     print(e)
# #6 Use a try-except-else block:If no error oçcurs, print "No errors! Everything went fine."
# try:
#     num = int(input("Enter a number: "))
# except ValueError:
#     print("Invalid input.")
# else:
#     print("No errors! Everything went fine.")
# #Add a finalif bfock to any of the above programs to print "Program execution complete." every time
# try:
#     num = int(input("Enter a number: "))
#     print("Number:", num)
# except ValueError:
#     print("Invalid input.")
# finally:
#     print("Program execution complete.")
# #Write a small program to convert a string to an integer.
# try:
#     text = input("Enter a number: ")
#     number = int(text)
#     print("Integer:", number)
# except ValueError:
#     print("Conversion failed!")

 #Ask the user to enter a file name. Try opening and reading it.
# try:
#     filename = input("Enter file name: ")

#     with open(filename, "r") as file:
#         print(file.read())

# except FileNotFoundError:
#     print("File not found!")

# finally:
#     print("File operation finished.")
#
balance = 5000

try:
    amount = int(input("Enter withdrawal amount: "))

    if amount > balance:
        raise ValueError("Insufficient balance!")

    balance -= amount
    print("Withdrawal successful.")
    print("Remaining Balance:", balance)

except ValueError as amt:
    print(amt)
