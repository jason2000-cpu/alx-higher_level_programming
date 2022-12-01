#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    
    argc = len(argv) - 1
    print(argc)
    if argc == 0:
        print("0 arguments.")

    elif argc > 1:
        print(f"{argc-1} arguments:")

    else:
        print(f"{argc} argument:")
    for i in range(argc-1):
        i += 1
        print(f"{i}: {argv[i]}")
