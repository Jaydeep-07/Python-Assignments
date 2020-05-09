def rec_fact(n):
	if(n==1):
		return n
	else:
		return n*rec_fact(n-1)
		

print("Enter The Number")
no=input()
no=int(no)

fact=rec_fact(no)
print(fact)