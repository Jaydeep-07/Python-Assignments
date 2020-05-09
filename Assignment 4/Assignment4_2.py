no1 = int(input("Enter No 1:"))
no2 = int(input("Enter No 2:"))

fp = lambda no1,no2 : no1 * no2
ret = fp(no1,no2)
print("Multiplication is {} with lambda function".format(ret))

