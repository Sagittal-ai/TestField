def add(x, y):
    """Add two integers.
    
    Args:
        x (int): The first integer.
        y (int): The second integer.
    
    Returns:
        int: The sum of x and y.
    """
    return x + y

def subtract(x, y):
    """Subtract two integers.
    
    Args:
        x (int): The first integer.
        y (int): The second integer.
    
    Returns:
        int: The result of subtracting y from x.
    """
    return x - y

if __name__ == '__main__':
    while True:
        print("Simple Calculator")
        print("Options:")
        print("1. Add")
        print("2. Subtract")
        print("Enter 'exit' to end the program.")
        choice = input("Choose an operation (1/2): ")
        if choice == 'exit':
            break
        if choice not in ['1', '2']:
            print("Invalid choice. Please select 1 or 2.")
            continue
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        if choice == '1':
            print(f"{x} + {y} = {add(x, y)}")
        elif choice == '2':
            print(f"{x} - {y} = {subtract(x, y)}")