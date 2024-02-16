
def __main__():
    print("Please select an interface:\n1. Command-line\n2. Graphical")
    choice = input("Enter your choice (1 to 2): ")

    if choice=="1":
        from llama_core import cli
    elif choice=="2":
        from llama_core import gui
    else:
        print("Not a valid number.")

if __name__=="__main__":
    __main__()
