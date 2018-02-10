#!/usr/bin/env python3

def count(my_list):
    c = 0
    for _ in my_list:
        c = c + 1
    return c

def find_max(my_list):
     max = -1
     idx = 0
     max_idx = 0
     for e in my_list:
         if e > max:
             max = e
             max_idx = idx
         idx = idx + 1 
     return max_idx, max

the_list = [40, 50, 9, 4, 8, 8, 5]
list_count = count(the_list)
idx, max = find_max(the_list)

print("Count = " + str(list_count))
print("Max Value = " + str(max))
print("Max Index = " + str(idx))
