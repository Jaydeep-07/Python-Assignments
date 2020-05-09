def Print(n):
	for i in range(1, n + 1):
		n = 1
		for j in range(1, 6):
			if i>=j:
				print(n, end=" ")
				n=n+1
			else:
				print(" ",end=" ")
		print()
		
no = int(input("Enter No Of Rows :"))
Print(no)
