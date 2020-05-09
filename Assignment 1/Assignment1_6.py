def fun(num):
	if(num>0):
		print("Positive Number")
	elif(num<0):
		print("Negative Number")
	else:
		print("Zero")
print("Enter The Number")
no=input()
no=int(no)
fun(no)