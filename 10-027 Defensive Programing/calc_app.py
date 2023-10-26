import os

def perform_calculation(num1, num2, operator):
    """
    Performs a calculation based on two numbers and an operator.

    Args:
    num1 (float): The first number.
    num2 (float): The second number.
    operator (str): The operator to use for the calculation (+, -, *, or /).

    Returns:
    float: The result of the calculation.
    """
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return num1 / num2
    else:
        raise ValueError("Invalid operator.")

def record_equation(num1, num2, operator, result):
    """
    Records an equation and its result in a file called equations.txt.

    Args:
    num1 (float): The first number.
    num2 (float): The second number.
    operator (str): The operator used for the calculation (+, -, *, or /).
    result (float): The result of the calculation.
    """
    with open("equations.txt", "a") as f:
        f.write(f"{num1} {operator} {num2} = {result}\n")

def print_equations():
    """
    Prints all previous equations stored in a file called equations.txt.
    """
    if not os.path.exists("equations.txt"):
        print("No equations found.")
        return
    with open("equations.txt", "r") as f:
        equations = f.readlines()
        if not equations:
            print("No equations found.")
            return
        for equation in equations:
            print(equation.strip())

def main():
    """
    Main function that runs the calculator application.
    """
    while True:
        print("Welcome to the calculator app!")
        print("1. Perform a calculation")
        print("2. Print previous equations")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")
        if choice == '1':
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                operator = input("Enter the operator (+, -, *, or /): ")
                result = perform_calculation(num1, num2, operator)
                print(f"{num1} {operator} {num2} = {result}")
                record_equation(num1, num2, operator, result)
            except ValueError as e:
                print(e)
        elif choice == '2':
            print_equations()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
