# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 19:33:43 2022

@author: be
"""

import numpy as np

#Down to 1 assignment


#Example tester (n=11). if n is odd replace n with 3*n+1, if odd replace with n/2
#Example should print out 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1 .... it took 14 steps



#
count = []

for x in range(5,21):
    counter = 0
    while x != 1:
        if (x % 2) == 0:
            x = x/2
            print(x)
            counter += 1
            
        elif (x % 2) != 0:
            x = 3*x+1
            print(x)
            counter += 1
    print("This took", counter, "steps.")
    count.append(counter)
print(count)
    
    
