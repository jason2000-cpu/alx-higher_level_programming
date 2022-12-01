#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    if len(argv) < 1:
        print("0 arguments.")
    elif len(argv) > 1:
        print(f"{len(argv)-1} arguments:")
    else:
        print(f"{len(argv)} argument:")
    for i in range(len(argv)-1):
        i+=1
        print(f"{i}: {argv[i]}")
