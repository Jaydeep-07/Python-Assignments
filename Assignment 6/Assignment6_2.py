class Circle:
	PI=3.14;
	def __init__(self):
		self.Radius = 0.0
		self.Area = 0.0
		self.Circumference = 0.0
	
	def Accept(self):
		Radius = float(input("Enter Radius :"))
		return Radius;
	def CalculateArea(self,value):
		Area=Circle.PI*value*value
		return Area;
	def CalculateCircumference(self,value):
		Circumference=2*Circle.PI*value
		return Circumference
	def Display(self):
		print(self.no1,self.no2)


def main():
	obj1 = Circle()
	
	a=float(obj1.Accept());
	print(a)
	
	b=obj1.CalculateArea(a);
	print(b)
	
	c=obj1.CalculateCircumference(a);
	print(c)

if __name__=="__main__":
	main();