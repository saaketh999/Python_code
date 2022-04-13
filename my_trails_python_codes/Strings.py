stri='hello world'
print(stri)
print(stri[0])
#Double quotetion marks

stri_with_quotes="He said 'you're amazing!!'  "
print(stri_with_quotes)
"""Escaping (putting a backslash infront of the character) is used in python to remove meaning from a charecter"""
anothe_with_quotes="He said \"You're amazing!!\" Yesterday"
print(anothe_with_quotes)

"""Adding Stings together"""

name = 'jose'
greeting='Hello, Mr.' + name
print(greeting)

"""
You cannot add intergers to strings, must convert integers to strings 
Eg: age = 30 --> Integer
age ='30' is a string 
or 
you can pass in
age_as_string = str(age) 
"""

age='30'
print('you are ' + age)