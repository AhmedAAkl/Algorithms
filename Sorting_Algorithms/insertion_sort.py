# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 22:45:23 2022

@author: A.Akl
"""

################ algorithms implementation   ###############


########           insertion sort     ##########

def insertion_sort(arr):
    
    for j in range(1,len(arr)):
        key = arr[j]
#        print(key)
        i = j -1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i = i - 1
        arr[i+1] = key
    return arr


test_arr = [5,2,4,6,1,3,55,34,8,9]
ordered_arr = insertion_sort(test_arr)
print(ordered_arr)
