#!/usr/bin/python3

def multiple_returns(sentence):
    str_len = len(sentence)
    str_first = sentence[0]
    return (str_len, str_first)

    '''
            OR DO THIS
    sen_tuple = str_len, str_first
    return sen_tuple
    '''
