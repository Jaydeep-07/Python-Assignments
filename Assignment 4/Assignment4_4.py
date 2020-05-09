import functools
def Chk(no):
	return no%2==0
def Square(no):
	return no*no
def Add(a,b):
	return a+b

lst=[]
num = int(input("Enter how many elements you want:"))
for i in range(0,int(num)):
	number=int(input("Enter numbers in array: "))
	lst.append(int(number))

no = list(filter(Chk,lst))
print("Data after filter ",no)

ModArray = list(map(Square,no))
print("Data after map", ModArray)

product = functools.reduce(Add,ModArray)
print("Addition of numbers",product)