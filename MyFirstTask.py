for i in range(0,10):
    print("GCI is great")
# Python code to reverse a string
# using loop

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

name=input("what is your name? ")
print ("Hello",name,"pleased to meet you!")
print ("Did you know your name backwards is",reverse(name),"?")