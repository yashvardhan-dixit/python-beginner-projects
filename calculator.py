def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "❌ Cannot divide by zero"
    return x / y

while True:
    print("\n🧮 Simple Calculator")
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == '5':
        print("👋 Exiting calculator. Bye!")
        break

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("⚠️ Please enter valid numbers.")
            continue

        if choice == '1':
            print(f"✅ Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"✅ Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"✅ Result: {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print(f"✅ Result: {result}")
        else:
            print("❌ Invalid choice. Please enter 1–5.")