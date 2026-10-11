class BankAccount:
	def __init__(self):
		self.balance=0
		print("welcome to state bank of india")

	def deposite(self):
		amount=float(input("enter the amount to be deposite: "))
		self.balance+=amount
		print("\nAmount deposited: ",amount)

	def withdraw(self):
		amount=float(input("enter the amount to withdraw: "))
		if self.balance>=amount:
			self.balance-=amount
			print("\namount withdraw: ",amount)

	def display(self):
		print("\nNet available balance= ",self.balance)

a1=BankAccount()
a1.deposite()
a1.withdraw()
a1.display()