'''
1. Exceptional Weather Forecast
Task 1: Start
Begin by setting up a simple user input loop that asks the user to enter the temperature in Fahrenheit.
Ensure that your program only accepts numerical input and provides a friendly error message if the user enters something that can't be converted to a number.

Task 2: Temperature Conversion
Write a function that converts the Fahrenheit temperature to Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9.
Use a try block to catch any potential errors during the conversion process, such as division by zero or overflow errors.

Task 3: User Experience
Implement an else block that prints the converted temperature in a user-friendly format.
Add a finally block that thanks the user for using the weather forecast application, ensuring that this message is displayed 
regardless of whether an exception was caught or not.

'''
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

while True:
    try:
        temp_input = float(input("Please enter the temperature in Fahrenheit: "))
        celsius_temp = fahrenheit_to_celsius(temp_input)
    except ValueError:
        print("Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print(f"The temperature in Celsius is: {celsius_temp:.2f}")
        break
    finally:
        print("Thank you for using the weather forecast application.")
