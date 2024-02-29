#!/usr/bin/env python3
def print_fibonacci(length):

    if length == 0:
        print([])

    elif length == 1:
        print([0])

    elif length == 2:
        fibonacci = [0,1]
        print(fibonacci)        
    
    else:
        fibonacci = [0,1]
        for i in range(2, length):
            c = fibonacci [-1] + fibonacci[-2]
            fibonacci.append(c)
        print(fibonacci)    
        
        
print_fibonacci(10)                       