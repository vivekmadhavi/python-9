class Employee:
	def __init__(self,name,address,salary):
		self.name=name
		self.address=address
		self.salary=salary

	def show(self):
		print("name =",self.name)
		print("address =",self.address)
		print("salary =",self.salary)
	
	def computeTaxes(self):
		if self.salary < 50000:
			r1= self.salary*(10/100)
			print("amt = ",r1)
		else :
			r1= (20/100)* self.salary
			print("amt =",r1)

e1 = Employee("vivek","chirle",51000)
e1.show()
e1.computeTaxes()

