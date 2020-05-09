
import sys
import os.path

def main():
    f1 = open(sys.argv[1], "r")
    f2 = open(sys.argv[2], "r")
    flg=False
    for line1 in f1:
        for line2 in f2:
            if line1 == line2:
                pass
            else:
                print("file nont equel")
                flg=True
            break
    f1.close()
    f2.close()
    if flg==False:
        print("file containt is same")

if __name__=="__main__":
	main();