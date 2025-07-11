import random
import string

def generate_password(length=12, use_symbols=True):
    characters = string.ascii_letters + string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Random Password Generator")
    
    try:
        length = int(input("Enter password length (default 12): ") or 12)
        use_symbols = input("Include symbols? (y/n, default y): ").strip().lower() != 'n'
        password = generate_password(length, use_symbols)
        print(f"\n✅ Your generated password: {password}")
    except ValueError:
        print("❌ Please enter a valid number!")

if __name__ == "__main__":
    main()
