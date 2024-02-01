#wapp to perform crud operation for covid patien in india 
# crud creaate read update delete

data = {}

while True:
	op =int(input("1 add new state , 2 view state, 3 update state , 4 delete state , 5 exit "))
	
	if op == 1:
		sn=input("enter state name ")
		if data.get(sn) != None:
			print("already exist")
		else:
			co =int(input("enter count "))
			data[sn] = co
			print(sn ,"added")
	elif op ==2:
		print(data)
	elif op == 3:
		sn =input("enter the state ")
		if data.get(sn) != None:
			print(sn , "does not exist")
		else:
			co = int(input("enter the updates count "))
			data[sn] = co
			print(sn , "updates")
	elif op == 4:
		sn =input("enter the state ")
		if data.get(sn) != None:
			print(sn , "does not exist")
		else:
			data.pop(sn)
			print(sn,"deleted")
	elif op == 5:
		break
	else:
		print("sorry i dont understand")
			
	 