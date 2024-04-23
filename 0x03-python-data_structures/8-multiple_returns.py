#!/usr/bin/python3

def multiple_returns(sentence):
    """creates a tuple"""
    lenght = len(sentence)
    first = sentence[:1]
    if len(sentence) == 0:
        first == None
    return lenght, first
