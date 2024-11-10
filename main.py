import os
from src.text_to_binary import text_to_binary
from src.binary_to_text import binary_to_text

def is_valid_binary(binary_code):
    """Check if the binary code is valid (only contains 0s and 1s and is divisible by 8)."""
    if all(bit in '01' for bit in binary_code) and len(binary_code) % 8 == 0:
        return True
    return False

def print_welcome():
    """Display a welcome message."""
    print("Welcome to the Binary Converter Tool!")
    print("This tool can either convert text to binary or decrypt binary code into text.")

def main():
    while True:
        print_welcome()

        print("\nChoose an option:")
        print("\n---------------------------------------------")
        print("1. Decrypt Binary Code")
        print("2. Convert Text to Binary")
        print("---------------------------------------------")

        option = input("Enter 1 or 2 > ")

        if option == "1":
            binary_code = input("Enter binary code: ")
            
            if is_valid_binary(binary_code):
                decoded_text = binary_to_text(binary_code)
                print(f"\033[32m[Valid]\033[0m {decoded_text}")
            else:
                print(f"\033[31m[Invalid]\033[0m The binary code is invalid.")
            input("Press Enter to return to the menu...")
            os.system('cls')

        elif option == "2":
            text = input("Enter text to convert to binary: ")
            binary_code = text_to_binary(text)
            print("Binary code: " + binary_code)
            input("Press Enter to return to the menu...")
            os.system('cls')

        else:
            print("Invalid option. Try again.")
            input("Press Enter to continue...")
            os.system('cls')

if __name__ == "__main__":
    main()
