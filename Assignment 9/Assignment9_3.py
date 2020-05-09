import shutil
import sys
import os

def main():
	path=sys.argv[1];
	flag=os.path.isabs(path);
	if flag==False:
		path=os.path.abspath(path);
	

	if(shutil.copy(sys.argv[1],'Demo.txt')):
		print("File Copied");
	else:
		print("File Not Copied");
		
	
		
if __name__=="__main__":
	main();