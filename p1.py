class Product:
	def __init__(self,id,name,price):
		self.id=id
		self.name=name
		self.price=price

	def show(self):
		print("id =",self.id)
		print("name =",self.name)
		print("price =",self.price)

p1 = Product(1,"sm",500)
p1.show()

p2=Product(2,"mp",400)
p2.show()

p3=Product(3,"hod",5400)
p3.show()
