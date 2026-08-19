print("========================")
print("     SIMPLE CALCULATOR")
print("========================")

while True:

    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "5":
        print("\nThank you for using Simple Calculator!")
        break

    if choice in ["1", "2", "3", "4"]:

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = num1 + num2
            print("Result:", result)

        elif choice == "2":
            result = num1 - num2
            print("Result:", result)

        elif choice == "3":
            result = num1 * num2
            print("Result:", result)

        elif choice == "4":
            if num2 == 0:
                print("Cannot divide by zero!")
            else:
                result = num1 / num2
                print("Result:", result)

    else:
        print("Invalid choice! Please try again.")