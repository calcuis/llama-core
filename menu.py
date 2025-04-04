print("Please select an interface:\n1. Command-line\n2. Graphical")
choice = input("Enter your choice (1 to 2): ")

if choice=="1":
    from .cli import *
elif choice=="2":
    from .gui import *
else:
    print("Not a valid number.")