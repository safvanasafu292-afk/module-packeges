try:
    number=int (input("enter a number:"))
    result=10/number
    print("result",result)
except ValueError:
    print("please enter a valid number")
except ZeroDivisionError:
    print("cannot divided by zero")