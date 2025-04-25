try:
    print("Welcome to the Exception Playground ")

    # NameError - trying to use a variable that doesn't exist
    print(undeclared_variable)

    # IndexError - accessing an out-of-range list index
    my_list = [10, 20, 30]
    print(my_list[5])

    # ZeroDivisionError - dividing by zero
    a = 5
    b = 0
    print(a / b)

except NameError:
    print("Caught a NameError!  Looks like you used a variable that hasn’t been defined.")

except IndexError:
    print("Caught an IndexError!  You tried to access a list index that doesn’t exist.")

except ZeroDivisionError:
    print("Caught a ZeroDivisionError!  You tried to divide by zero, naughty!")

except Exception as e:
    print("Caught a general exception :", e)

finally:
    print("End of exception handling demo. Clean and safe ")
