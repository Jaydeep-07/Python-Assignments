class Demo:
	value=1;
	def __init__(self,value1,value2):
		self.no1 = value1
		self.no2 = value2
	def fun(self):
		print(self.no1,self.no2)
	def gun(self):
		print(self.no1,self.no2)


def main():
	obj1 = Demo(11,21)
	obj2 = Demo(51,101)

	obj1.fun()
	obj2.fun()

	obj1.gun()
	obj2.gun()

if __name__=="__main__":
	main();