lst=[]
num = int(input("Enter how many elements you want:"))
for i in range(0,int(num)):
	number=int(input("Enter numbers in array: "))
	lst.append(int(number))
	
number2=int(input("Enter number: "))

print ("frquency=",lst.count(number2))