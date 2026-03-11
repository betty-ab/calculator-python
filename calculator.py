def calculator():
    history = []  
    print("====================================")
    print("      Python CLI Calculator         ")
    print("====================================")
    print("Welcome! Perform quick calculations easily.")

    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. View History") 
        print("6. Exit")

        choice = input("Enter choice (1/2/3/4/5/6): ")

        if choice == "6":
            print("\nThank you for using the Python CLI Calculator. Have a great day!")
            break
        
        
        if choice == "5":
            print("\n--- Calculation History ---")
            if not history:
                print("No calculations yet.")
            else:
                for entry in history:
                    print(entry)
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = f"{num1} + {num2} = {num1 + num2}"
                print(f"Result: {result}")
                history.append(result)

            elif choice == '2':
                result = f"{num1} - {num2} = {num1 - num2}"
                print(f"Result: {result}")
                history.append(result)

            elif choice == '3':
                result = f"{num1} * {num2} = {num1 * num2}"
                print(f"Result: {result}")
                history.append(result)

            elif choice == '4':
                if num2 == 0:
                    print("Error! Division by zero.")
                else:
                    result = f"{num1} / {num2} = {num1 / num2}"
                    print(f"Result: {result}")
                    history.append(result)
            else:
                print("Invalid choice!")

        except ValueError:
            print("Invalid input! Please enter numbers.")

if __name__ == "__main__":
    calculator()
