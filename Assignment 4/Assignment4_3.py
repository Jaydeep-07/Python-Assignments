import functools
def Chk(no):
	return no in range(70,91)
def Increase(no):
	return no+10
def Prod(a,b):
	return a*b

lst=[]
num = int(input("Enter how many elements you want:"))
for i in range(0,int(num)):
	number=int(input("Enter numbers in array: "))
	lst.append(int(number))

no = list(filter(Chk,lst))
print("Data after filter ",no)

ModArray = list(map(Increase,no))
print("Data after map", ModArray)

product = functools.reduce(Prod,ModArray)
print("Product of numbers",product)