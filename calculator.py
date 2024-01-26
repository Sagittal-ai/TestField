def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == '__main__':
    while True:
        print("Simple Calculator")
        print("Options:")
        print("1. Add")
        print("2. Subtract")
        print("3. Exit")
        choice = input("Enter choice(1/2/3): ")

        if choice in ('1', '2', '3'):
            if choice == '3':
                print("Exiting...")
                break
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))

            if choice == '1':
                print("The result is", add(num1, num2))
            elif choice == '2':
                print("The result is", subtract(num1, num2))
        else:
            print("Invalid Input")
