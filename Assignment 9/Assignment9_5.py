from sys import*
import os.path


def main():
	flag=False;
	total=0;
	file=open(argv[1],'r');
	
	Str=input("Enter The String");
	Str=Str.split();
	#print(Str)
	
	for line1 in Str:
		for line2 in file:
			if line1 in line2:
				total+=1;
				flag=True;
				pass;
	if(flag==True):
		print("Frequency",total);
	else:
		print("String Not Found");
	
if __name__=="__main__":
	main();