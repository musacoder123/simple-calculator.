# Scientific Calculator
# Created using Python

import math


def calculator():
    history = []

    while True:
        print("\n===== SCIENTIFIC CALCULATOR =====")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Power (x^y)")
        print("6. Square Root")
        print("7. Sine (sin)")
        print("8. Cosine (cos)")
        print("9. Tangent (tan)")
        print("10. Logarithm (log10)")
        print("11. Factorial (!)")
        print("12. View Calculation History")
        print("0. Exit")

        choice = input("Choose an operation: ").strip()

        # Operator shortcuts
        if choice in ["+", "-", "*", "/", "^"]:
            choice = {
                "+": "1",
                "-": "2",
                "*": "3",
                "/": "4",
                "^": "5"
            }[choice]

        # Exit
        if choice == "0":
            print("Thank you for using the calculator!")
            break

        # View calculation history
        if choice == "12":
            print("\n===== CALCULATION HISTORY =====")

            if not history:
                print("No calculations yet.")
            else:
                for item in history:
                    print(item)

            continue

        try:
            # Basic arithmetic operations
            if choice in ["1", "2", "3", "4", "5"]:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == "1":
                    result = num1 + num2
                    calculation = f"{num1} + {num2} = {result}"

                elif choice == "2":
                    result = num1 - num2
                    calculation = f"{num1} - {num2} = {result}"

                elif choice == "3":
                    result = num1 * num2
                    calculation = f"{num1} * {num2} = {result}"

                elif choice == "4":
                    if num2 == 0:
                        print("Error: Cannot divide by zero.")
                        continue

                    result = num1 / num2
                    calculation = f"{num1} / {num2} = {result}"

                elif choice == "5":
                    result = num1 ** num2
                    calculation = f"{num1} ^ {num2} = {result}"

            # Square root
            elif choice == "6":
                num = float(input("Enter a number: "))

                if num < 0:
                    print("Error: Cannot calculate the square root of a negative number.")
                    continue

                result = math.sqrt(num)
                calculation = f"sqrt({num}) = {result}"

            # Trigonometric operations
            elif choice in ["7", "8", "9"]:
                angle = float(input("Enter angle in degrees: "))
                radians = math.radians(angle)

                if choice == "7":
                    result = math.sin(radians)
                    calculation = f"sin({angle}) = {result}"

                elif choice == "8":
                    result = math.cos(radians)
                    calculation = f"cos({angle}) = {result}"

                elif choice == "9":
                    if math.isclose(
                        math.cos(radians), 0.0, abs_tol=1e-12
                    ):
                        print("Error: Tangent is undefined for this angle.")
                        continue

                    result = math.tan(radians)
                    calculation = f"tan({angle}) = {result}"

            # Logarithm
            elif choice == "10":
                num = float(input("Enter a positive number: "))

                if num <= 0:
                    print("Error: Logarithm requires a positive number.")
                    continue

                result = math.log10(num)
                calculation = f"log10({num}) = {result}"

            # Factorial
            elif choice == "11":
                num = int(input("Enter a non-negative integer: "))

                if num < 0:
                    print("Error: Factorial is not defined for negative integers.")
                    continue

                result = math.factorial(num)
                calculation = f"{num}! = {result}"

            else:
                print("Invalid choice. Please try again.")
                continue

            # Display and save the result
            print("Result:", result)
            history.append(calculation)

        except ValueError:
            print("Error: Please enter a valid number.")

        except OverflowError:
            print("Error: The result is too large.")

        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")


calculator()
