import functools
def Chk(no):
	cnt=0
	if no>1:
		for i in range(2,no+1):
			if i!=no:
				if no%i==0:
					cnt=cnt+1
		if cnt==0:
			return no
def Increase(no):
	return no*2
def Maxx(a,b):
	return max(a,b)

lst=list()
num = int(input("Enter how many elements you want:"))
for i in range(0,int(num)):
	number=int(input("Enter numbers in array: "))
	lst.append(int(number))

no = list(filter(Chk,lst))
print("Data after filter ",no)

ModArray = list(map(Increase,no))
print("Data after map", ModArray)

product = functools.reduce(Maxx,ModArray)
print("Maximum",product)