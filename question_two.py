'''
The Recipe Ratio Adjuster
Task 1: Start
Ask the user for the number of servings the recipe is originally for and the number of servings they wish to make.
Ensure that the user inputs are valid numbers and handle any ValueError that arises from improper input.

Task 2: Quantity Calculation
Calculate the adjustment factor by dividing the desired servings by the original servings.
Use a try block to catch any arithmetic errors that may occur during the calculation.

Task 3: Serving Success
If the calculation is successful, display the adjusted recipe quantities to the user.
Use a finally block to print a message encouraging the user to enjoy their cooking, regardless of the outcome of the calculation.
'''

def recipe_ratio(number_of_servings, number_of_new_servings):
    try:
        return number_of_new_servings / number_of_servings 
    except ZeroDivisionError:
        return "Division by zero is not allowed." 


while True:
        try:#
            number_of_servings = float(input("Enter the number of servings (original): "))
            number_of_new_servings = float(input("Enter the new amount of servings required: "))
            result = recipe_ratio(number_of_servings, number_of_new_servings)
            print(f"Recipe ratio is {result}") 
        except ValueError:#
            print("Please only enter numbers. Try again.")
             
        continue_input = input("Would you like to get the recipe servings for another meal? (yes/no): ").lower()   
        if continue_input != 'yes': 
            print("Enjoy cooking!")
            break
