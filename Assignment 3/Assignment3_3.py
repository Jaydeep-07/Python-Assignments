lst=[]
num = int(input("Enter how many elements you want:"))
for i in range(0,int(num)):
	number=int(input("Enter numbers in array: "))
	lst.append(int(number))
print ("min=",min(lst))