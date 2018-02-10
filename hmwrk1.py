#!/usr/bin/env python3

def calc_sum(my_list): 
    sum = 0
    for digit in my_list:
       sum = sum + digit 
    return (sum)

def calc_ind(my_list):
    ind = 0
    for digit in my_list:
       ind = ind + 1 
    return (ind)


list = [4, 2 , 7 , 8, 9, 10, 2, 8, 6]
list_sum = calc_sum(list)
list_avg = list_sum / calc_ind(list)

print (list)
print (list_sum, list_avg)
