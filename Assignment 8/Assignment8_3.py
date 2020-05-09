import threading

def evenlist(num):
    num=list(num)
    sum=0
    for i in range(len(num)):
        if  num[i]%2==0:
            sum=sum+num[i]
    print("even",sum)
def oddlist(num):
    num = list(num)
    sum=0
    for i in range(len(num)):
        if num[i] % 2 != 0:
            sum = sum + num[i]
    print("odd",sum)
if __name__ == "__main__":
    num = [2,3,4,5,6,7,8,9,10]
    thread1 = threading.Thread(target=evenlist, args=(num,))
    thread2 = threading.Thread(target=oddlist, args=(num,))
# Will execute both in parallel
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print(" exit fom main.")