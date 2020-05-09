from sys import*
import os.path


def main():
	
	path=argv[1];
	flag=os.path.isabs(path);
	if flag==False:
		path=os.path.abspath(path);
		
	
	if(os.path.exists(path)):
		print("File Is Exists");
	else:
	print("File Does Not Exists");


if __name__=="__main__":
	main();