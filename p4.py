#single inheritance 

class Person:
	def __init__(self,id,name,address):
		self.id=id
		self.name=name
		self.address=address

	def show(self):
		print("id=", self.id)
		print("name=", self.name)
		print("address=", self.address)

class Student(Person):
	def __init__(self,id,name,address,marks):
		super().__init__(id,name,address)
		self.marks=marks

	def show(self):
		super().show()
		print("marks =", self.marks)

p1=Person(10,"amt","uran")
p1.show()

s1=Student(20,"vivek","uran",80)
s1.show()	