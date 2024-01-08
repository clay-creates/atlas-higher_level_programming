#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence is None:
        sentence = None
    elif sentence != None:
        length = len(sentence)
    else:
        lenght = 0

    return (length, sentence[:1])
