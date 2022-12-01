#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    
    argc = len(argv) - 1
    if argc == 0:
        print("0 arguments.")

    elif argc == 1:
        print("1 argument:")

    else:
        print(f"{argc} arguments:")
    for i in range(argc):
        i += 1
        print(f"{i}: {argv[i]}")
