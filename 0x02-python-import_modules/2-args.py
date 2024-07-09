#!/usr/bin/python3

if __name__ == "__main__":
    
    import sys
    argv = sys.argv[1:]
    arguments_number = len(argv)
    
    if arguments_number == 0:
        print(f"{arguments_number} arguments.")
    elif arguments_number == 1:
        print(f"{arguments_number} argument:")
        print(f"1: {argv[0]}")
    else:
        print(f"{arguments_number} arguments:")
        for i in range(arguments_number):
            print(f"{i + 1}: {argv[i]}")
