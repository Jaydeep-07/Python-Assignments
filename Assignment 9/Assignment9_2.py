import sys
import os.path
def main():

	path=sys.argv[1];
	flag=os.path.isabs(path);
	if flag==False:
		path=os.path.abspath(path);
		print(path)
		if os.path.exists(path):
			print("file exist")
		else:
			print("file does not exist")

	fd = open(path,'r')
	print("Information about file : ",fd.read())


if __name__=="__main__":
    main()