#!/usr/bin/env python3

import datetime

name = input ('Please enter your name:')
age = int (input ('Please enter your age:'))


print (name, "will be 120 in", datetime.date.today().year + 120 - age)


