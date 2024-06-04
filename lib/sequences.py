#!/usr/bin/env python3
import ipdb


def print_fibonacci(length):
    if length == 0:
        fib = []
        #ipdb.set_trace()
        print(fib)
        return
    elif length == 1:
        fib = [0]
        #ipdb.set_trace()
        print(fib)        
        return
    else:
        fib = [0,1]
        while len(fib) < length:
            newNum = fib[-2] + fib[-1]
            fib.append(newNum)
        #ipdb.set_trace()
        print(fib)
        return    
#print_fibonacci(0)
#print_fibonacci(1)
#print_fibonacci(10)       