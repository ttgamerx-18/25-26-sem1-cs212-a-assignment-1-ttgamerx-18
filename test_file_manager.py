#!/usr/bin/env python3
"""
Python CLI File Manager - Fixed Version
With all TODOs completed at beginner level.
Uses only standard library modules.
"""

import os

def display_welcome():
    """Display welcome message to the user."""
    print("=" * 50)
    print("   Welcome to Python CLI File Manager!")
    print("=" * 50)
    print("This is a simple file manager to demonstrate Python fundamentals.")
    print("You can use it to explore files, calculate sizes, and more.")
    print("Type 'help' to see available commands.")
    print()  


def calculate_file_size():
    """Calculate the size of a file in KB with floating point division."""
    filename = input("Enter file name: ")
    if not os.path.exists(filename):
        print("File does not exist.")
        return
    
    size = os.path.getsize(filename)
    size_kb = size / 1024   
    print(f"Size of '{filename}': {size_kb:.2f} KB")


def get_user_choice():
    """Get a command choice from the user."""
    choice = input("Enter a command: ")
    return choice  


def process_user_command(
    choice, running,
    show_goodbye=True,
    goodbye_message="Thank you for using the File Manager. Goodbye!",
    invalid_choice_prefix="Invalid choice:",
    valid_commands="help, quit, calculate"
):
    """Process the command entered by the user with default keyword args."""
    if choice == "help":
        print("Available commands:", valid_commands)
        return True
    elif choice == "quit":
        if show_goodbye:
            print(goodbye_message)
        return False
    elif choice == "calculate":
        calculate_file_size()
        return True
    else:
        print(f"{invalid_choice_prefix} {choice}")
        print("Valid options are:", valid_commands)
        return True


def main():
    """Main program loop for the file manager."""
    display_welcome() 
    
    running = True  
    
    while running:
        choice = get_user_choice()
        running = process_user_command(choice, running)


if __name__ == "__main__":
    main()
