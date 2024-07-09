#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    arguments = sys.argv
    arguments_number = len(arguments)
    
    if len(arguments) == 0:
        print(f"{arguments_number} arguments.", end="")
    elif len(arguments) == 1:
        print(f"{arguments_number} argument:", end="")
        print(f"{arguments[0]}")
    elif len(arguments) > 1:
        print(f"{arguments_number} arguments:", end="")
        for i in range(1, arguments_number):
            print(f"{arguments[i]}")
