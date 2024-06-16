import math_operations as mo


def calculate():
    while True:
        print("Select Operation.")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choose = input("Enter choice (1/2/3/4/5): ")

        if choose == '5':
            print("Exiting Calculator")
            break

        if choose in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

            except ValueError:
                print("Please Enter Number only")
                continue

            if choose == '1':
                result = mo.add(num1, num2)

            elif choose == '2':
                result = mo.subtract(num1, num2)

            elif choose == '3':
                result = mo.multiply(num1, num2)

            elif choose == '4':
                result = mo.divide(num1, num2)

            print(f"The result is: {result}")

        else:
            print("Invalid input. Please select a number between 1 and 5.")


calculate()
