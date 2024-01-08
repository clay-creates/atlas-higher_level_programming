#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence is None:
        sentence[:1] = None
    elif sentence is not None:
        length = len(sentence)
    else:
        length = 0

    return (length, sentence[:1])
