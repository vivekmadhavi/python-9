class Account:
	def __init__(self,accno,name,balance):
		self.accno=accno
		self.name=name
		self.balance=balance

	def show(self):
		print("accono =",self.accno)
		print("name =",self.name)
		print("balance =",self.balance)
	
	def deposite(self,amt):
		self.balance=self.balance + amt

	def withdraw(self,amt):
		self.balance=self.balance - amt

a1 = Account(100,"vivek",5000)
a1.show()
a1.deposite(100)
a1.show()
a1.withdraw(50)
a1.show()


