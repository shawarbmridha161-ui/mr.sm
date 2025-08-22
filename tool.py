# tool.py
def greet_user():
    print("Hello! Welcome to mr.sm's first tool.\n")

def calculator():
    print("This tool can do simple addition and subtraction.")
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Choose operation (+ or -): ")
        if op == "+":
            print(f"Result: {a + b}")
        elif op == "-":
            print(f"Result: {a - b}")
        else:
            print("Invalid operation!")
    except ValueError:
        print("Please enter valid numbers!")

def main():
    greet_user()
    while True:
        print("\nMenu:")
        print("1. Calculator")
        print("2. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            calculator()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()