def fun(no):
	cnt = 0
	while(no>0):
		no=no // 10
		cnt=cnt+1
	print("Total=",cnt)


print("Enter The Number")
no=input()
no=int(no)
fun(no)
		
