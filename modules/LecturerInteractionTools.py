import os

def checkDestination():
        path = os.getcwd()
        print(f"""The module will be created in: {path}.
Is this correct? Y/N""")
        correct = input()
        if correct.lower() == "y":
             return path
        else:
             path = os.path.normpath(input("Enter correct path: "))
             return path

def getModuleName():
    name = "".join(x for x in input("What is the module name: ") if x.isalnum())
    while not name:
        print("Module name cannot be empty.")
        name = "".join(x for x in input("What is the module name: ") if x.isalnum())
    return name

def getModuleDuration():
    length = 0
    while not length:
        try:
            length = int(input("What is the duration of the module in weeks?: "))
        except ValueError as e:
            print("Duration must be a numeric value")
        except:
            raise
    return length