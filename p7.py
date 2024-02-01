class Book:
	def __init__(self,id,title,author,price):
		self.id=id
		self.author=author
		self.price=price

	def show(self):
		print("id =",self.id)
		print("title =",self.title)
		print("price =",self.price)
	
	def __add__(self,other):
		res=self.price+other.price
		return res

	def __sub__(self,other):
		res=self.price - other.price
		return res

	def __mul__(self,other):
		res=self.price * other.price
		return res

	def __div__(self,other):
		res=self.price+other.price
		return res

b1 = Book(100,"vivek","ml",500)
b2 = Book(100,"vivek","ml",300)

r1 = b1 + b2
print(r1)

r1 = b1 - b2
print(r1)

r1 = b1 * b2
print(r1)
#r1 = b1 / b2
#print(r1)
