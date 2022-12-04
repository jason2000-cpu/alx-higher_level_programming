#!/usr/bin/python3

def multiple_returns(sentence):
    info = ()
    if not sentence:
        info = info + (len(sentence), None)
        print(info)
    else:
        info = info + (len(sentence), sentence[0])
        print(info)

    return info
