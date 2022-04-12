def add(a,b):
	return a+b
def sub(a,b):
	return a-b
def mul(a,b):
	return a*b
def div(a,b):
	return a/b
print("""select the arithmetic function
1.add
2.sub
3.mul
4.div
""")
choose = int(input("choose any arithmetic function"))
a = float(input("enter the number:"))
b = float(input("enter the number:"))
if (choose ==1):
	print(add(a,b))
	print(type(add(a,b)))
elif (choose==2):
	print(sub(a,b))
elif (choose==3):
	print(mul(a,b))
elif (choose==4):
	print(div(a,b))
else:
	print("choose the correct arithmetic function")
