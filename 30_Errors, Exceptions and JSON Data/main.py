try:
    # Code that may raise an exception
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"The result is {result}")

except ValueError:
    # This block runs if a ValueError occurs (e.g., invalid input)
    print("Error: You did not enter a valid number.")

except ZeroDivisionError:
    # This block runs if a ZeroDivisionError occurs (e.g., dividing by zero)
    print("Error: You cannot divide by zero.")

except Exception as e:
    # This block handles any other kind of exception
    print(f"An unexpected error occurred: {e}")

finally:
    # This block always runs, whether an exception was raised or not
    print("Execution complete.")
