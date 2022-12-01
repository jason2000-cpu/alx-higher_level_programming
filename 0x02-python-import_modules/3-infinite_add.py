#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    sum = 0
    argc = len(argv)-1
    if argc == 0:
        print(0)

    for i in range(argc):
        i += 1
        sum = sum + int(argv[i])

    print(sum)
