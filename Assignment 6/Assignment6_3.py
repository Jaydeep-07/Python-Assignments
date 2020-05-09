class Arithmetic:
	def __init__(self):
		self.value1 = 0
		self.value2 = 0
		self.value3 = 0
	
	def Accept(self):
		value1 = int(input("Enter No  :"))
		return value1
		
	def Addition(self,value1,value2):
		self.value3=value1+value2;
		print("Addition=",self.value3);
	
	def Subtraction(self,value1,value2):
		self.value3=value1-value2;
		print("Subtraction=",self.value3);
	
	def Multiplication(self,value1,value2):
		self.value3=value1*value2;
		print("Multiplication=",self.value3);
	
	def Division(self,value1,value2):
		self.value3=value1//value2;
		print("Division=",self.value3);
	

def main():
	obj1 = Arithmetic()
	
	n1=obj1.Accept();
	#print(n1);
	n2=obj1.Accept();
	#print(n2);

	obj1.Addition(n1,n2);
	obj1.Subtraction(n1,n2);
	obj1.Multiplication(n1,n2);
	obj1.Division(n1,n2);
	
	
if __name__=="__main__":
	main();