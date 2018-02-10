#!/usr/bin/env python3

import datetime

def calc_year(my_age):
    year = 2018 + 120 - my_age 
    return(year)

name = input ('Please enter your name:')
age = int (input ('Please enter your age:'))


print (name)
print (calc_year(age))


