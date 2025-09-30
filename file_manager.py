#!/usr/bin/env python3
"""
Python CLI File Manager - Beginner Version
A simple file manager demonstrating Python basics:
variables, expressions, statements, and functions.
"""

import os
import sys


def display_welcome():
    """Display welcome message to the user."""
    print("=" * 50)
    print("   Welcome to Python CLI File Manager!")
    print("=" * 50)
    print("This is a simple file manager to practice")
    print("Python fundamentals.")
    print()


def calculate_file_size():
    """Ask for a filename and show its size."""
    filename = input("Enter the filename (with path if needed): ").strip()

    if not filename:
        print("Error: No filename provided.")
        return

    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return

    if not os.path.isfile(filename):
        print(f"Error: '{filename}' is not a regular file.")
        return

    size_bytes = os.path.getsize(filename)
    size_kb = size_bytes / 1024
    size_mb = size_bytes / (1024 * 1024)

    print(f"\nFile: {filename}")
    print(f"Size: {size_bytes} bytes")
    if size_bytes >= 1024:
        print(f"Size: {size_kb:.2f} KB")
    if size_bytes >= 1024 * 1024:
        print(f"Size: {size_mb:.2f} MB")


def get_user_choice():
    """Show menu and return user choice."""
    print("\nAvailable commands:")
    print("help - Show help message")
    print("calc - Calculate file size")
    print("info - Show program information")
    print("quit - Exit the program")
    print()
    choice = input("Enter your choice (help/calc/info/quit): ").strip().lower()
    return choice


def display_help():
    """Show help information."""
    print("\n" + "=" * 40)
    print("           HELP - Commands")
    print("=" * 40)
    print("help - Show this help message")
    print("calc - Calculate the size of a file")
    print("info - Show information about this program")
    print("quit - Exit the file manager")
    print("=" * 40)


def display_info():
    """Show program information."""
    print("\n" + "=" * 40)
    print("         PROGRAM INFORMATION")
    print("=" * 40)
    print("Program: Python CLI File Manager")
    print("Purpose: Beginner Python practice")
    print("Concepts: Variables, expressions, statements, functions")
    print("Features:")
    print("  - File size calculation")
    print("  - Simple command system")
    print("  - Help and info screens")
    print("  - Standard library only")
    print()
    print("Python Version:", sys.version.split()[0])
    print("=" * 40)


def process_user_command(choice, running, show_goodbye, goodbye_message, 
                        invalid_choice_prefix, valid_commands):
    """
    Process a user command and return the updated running state.
    
    This function demonstrates keyword arguments and is designed to test
    students' understanding of keyword-only arguments and default values.
    
    Args:
        choice (str): The user's command choice
        running (bool): Current state of the program loop
        show_goodbye (bool, keyword-only): Whether to show goodbye message when quitting
        goodbye_message (str, keyword-only): Custom goodbye message
        invalid_choice_prefix (str, keyword-only): Prefix for invalid choice messages
        valid_commands (str, keyword-only): String listing valid commands
    
    Returns:
        bool: Updated running state (False if user chose to quit, True otherwise)
    """
    if choice == "help":
        display_help()
    elif choice == "calc":
        calculate_file_size()
    elif choice == "info":
        display_info()
    elif choice == "quit":
        print(f"\n{goodbye_message}")
        print("Goodbye!")
        return False
    else:
        print(f"\n{invalid_choice_prefix} '{choice}'")
        print(f"Please enter one of: {valid_commands}")

    return running


def main():
    """Main loop of the program."""
    display_welcome()
    running = True

    while running:
        try:
            choice = get_user_choice()
            running = process_user_command(choice, running)
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user.")
            break
        except EOFError:
            print("\n\nEnd of input detected.")
            break

    print("Thank you for using Python CLI File Manager!")


if __name__ == "__main__":
    main()
