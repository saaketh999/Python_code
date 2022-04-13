"""For loop example 1 which prints the numbers from 4 to 19 but with gap of 2"""

#for index in range(4,20,2):
#    print(index)

"""For example 2 prints the numbers b/w 4 and 20"""
#for index in range(4,20):
    #print(index)
"""This below program shows how to use for loop on an ittretable objects such as list, dictonaries and tupples """
Employee_details = [
    {"name":"Saketh","GPA":8.01,"Job_exp":"3 years"},
    {"name":"Vijay","GPA":7.56,"Job_exp":"4.5 years"},
    {"name":"Karthik","GPA":7,"Job_exp":"10 years"},
    {"name":"Sam","GPA":8.7,"Job_exp":"1 years"},
]

for employee in Employee_details :
    name=employee["name"]
    grade=employee["GPA"]
    experience=employee["Job_exp"]
    print(f"Employee {name} has {experience} of work experience and had scored a grade point average of {grade} in there respective bachelors")

