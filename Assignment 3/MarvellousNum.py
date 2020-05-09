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
