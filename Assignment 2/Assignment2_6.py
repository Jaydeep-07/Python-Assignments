def Print(n):
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			if j<= n + 1 - i:
				print("*", end=" ")
			else:
				print(" ",end=" ")
		print()
		
no = int(input("Enter No Of Rows :"))
Print(no)
