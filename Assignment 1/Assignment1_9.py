def Fun(no):
	cnt=1
	for i in range(1,no):
		if(i%2==0 and cnt<=10):
			print(i,end=' ')
			i=i+1
			cnt=cnt+1
		
Fun(100)
		
	