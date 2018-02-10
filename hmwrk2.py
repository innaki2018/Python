#!/usr/bin/env python3

def calc_vowel(my_string): 
    num = 0
    for ltr in my_string:
       if (ltr=="a") or (ltr=="e") or (ltr=="i") or (ltr=="o") or (ltr=="u"):
          num = num + 1 
    return (num)


string = "example"
for c in string:
   print ("The latter is: " + c)

num_vowel = calc_vowel(string)

print (num_vowel)
