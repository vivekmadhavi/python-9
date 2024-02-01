#multi-level inheritance 

class Person:
	def __init__(self,id,name,address):
		self.id=id
		self.name=name
		self.address=address

	def show(self):
		print("id=", self.id)
		print("name=", self.name)
		print("address=", self.address)

class Teacher(Person):
	def __init__(self,id,name,address,salary):
		super().__init__(id,name,address)
		self.salary=salary

	def show(self):
		super().show()
		print("salary =", self.salary)
class Hod(Teacher):
	def __init__(self,id,name,address,salary,dept):
		super().__init__(id,name,address,salary)
		self.dept=dept

	def show(self):
		super().show()
		print("dept =", self.dept)

p1=Person(10,"amt","uran")
p1.show()
print("*" *150)
s1=Teacher(20,"vivek","uran",80)
s1.show()
print("*" *150)

s3=Hod(20,"ti","uran",20000,"it")
s3.show()	