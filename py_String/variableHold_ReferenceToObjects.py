#! python3
# A Shebang indicates which Bash or Python interpreter to use to interpret an executable file. 
# https://realpython.com/python-variables/#creating-variables-with-assignments
# Variables Hold References to Objects
# What happens when you create a variable with an assignment? 
#      This is an important question in Python because the answer differs from what you’d find in many other programming languages.

import pathlib, sys, os

# Python creates an ID as a unique reference to an object when you create a variable.
iteration=True
while iteration==True:
    iteration=False
    if iteration==True:
        continue
        try:
            a=300
            m=a
            if id(a) == id(m):
                print(f'Variable "a=" {a} and Variable  "m=" {m} have the same reference "ID" {id(m)}')
                print("Therefore they point to the same object in memory if you change 'm' then 'a' changes as well and vice-vesa")
            m=25
            m=m+int(a)
            if id(a) == id(m):
                print(f'Variable "a=" {a} and Variable  "m=" {m} have the same reference "ID" {id(m)}')
                print("Therefore they point to the same object in memory if you change 'm' then 'a' changes as well and vice-vesa")
            else:
                print(f'Variable "a=" {a} and Variable  "m=" {m} have the Diffrent reference "ID m=" {id(m)} and "ID a=" {id(a)}')   
        except Exception as e:
            print(f"We encountered an exception .....    {str(e)}")

    # Collections
    #  List
    a = [10, 25, 2]
    m = a
    if id(a) == id(m):
        print(f'Variable "a=" {a} and Variable  "m=" {m} have the same reference "ID" {id(m)}')
        print("Therefore they point to the same object in memory if you change 'm' then 'a' changes as well and vice-vesa")

    # The below works it creates a different reference even the commented out statement works "#v[i]=ai"
    v=[]
    for i, ai in enumerate(a):
        v.append(ai)
        #v[i]=ai

    if id(a) == id(v):
        print(f'Variable "a=" {a} and Variable  "v=" {v} have the same reference "ID" {id(v)}')
        print("Therefore they point to the same object in memory if you change 'm' then 'a' changes as well and vice-vesa")
    else:
        print(f'Variable "a=" {a} and Variable  "v=" {v} have the Diffrent reference "ID m=" {id(v)} and "ID a=" {id(a)}')
exit