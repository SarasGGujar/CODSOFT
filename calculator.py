# Calculator Program

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def calculator():
    while True:
        print("\nPlease select operation -\n" \
              "1. Add\n" \
              "2. Subtract\n" \
              "3. Multiply\n" \
              "4. Divide\n" \
              "5. Exit")

        # Taking Input
        select = input("Select operation (1, 2, 3, 4, 5): ")

        if select in ['1', '2', '3', '4']:
            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))

            if select == '1':
                print(f"{number_1} + {number_2} = {add(number_1, number_2)}")

            elif select == '2':
                print(f"{number_1} - {number_2} = {subtract(number_1, number_2)}")

            elif select == '3':
                print(f"{number_1} * {number_2} = {multiply(number_1, number_2)}")

            elif select == '4':
                if number_2 != 0:
                    print(f"{number_1} / {number_2} = {divide(number_1, number_2)}")
                else:
                    print("Math Error")

        elif select == '5':
            print("Thanks for using. See Ya!")
            break
        else:
            print("Invalid Input. Try Again")

# Run the calculator
calculator()
