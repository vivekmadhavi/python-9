#method overriding

class Employee:
	def __init__(self,id,name,address,salary):
		self.id=id
		self.name=name
		self.address=address
		self.salary=salary	

	def show(self):
		print(self.id , self.name , self.address ,   self.salary )

	def bonus(self):
		amt = self.salary * 0.10
		print("amt =", amt)
class Fresher(Employee):
	pass

f1=Fresher(1,"vivek","uran",10000)
f1.show()
f1.bonus()

class Senior(Employee):
	def bonus(self):
		amt = self.salary * 0.15
		print("amt =", amt)


s1=Senior(1,"vivek","uran",50000)
s1.show()
s1.bonus()

class Manager(Employee):
	def bonus(self):
		amt = self.salary * 0.20
		print("amt =", amt)


m1=Manager(1,"vivek","uran",50000)
m1.show()
m1.bonus()


