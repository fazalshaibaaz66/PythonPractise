class MyClass():
	#add
	def add(self, a,b):
		self.var = a
		self.van = b
		c = a + b
		return c

	#substract
	def sub(self, a, b):
		self.var = a
		self.van = b
		c = a - b
		return c

	#multiply
	def mul(self, a, b):
		self.var = a
		self.van = b
		c = a * b
		return c

	#divide
	def div(self, a, b):
		self.var = a
		self.van = b
		c = a/b
		return c

	def operation():
		print("......Welcome to the Calci world..........")

		#taking input in 2 variables
		var = int(input (f"gimme 2 values "))
		van = int(input(f" gimme 2nd value "))

		print("......What operation do you want to do..........")
		print("......1. Addition.......")
		print(".......2. Substraction......")
		print("........3. Multiplication........")
		print(".........4. Division........")

		choice = int(input())

		if choice == 1:
			print(f"Addition of {var} + {van} is..")
			print(objectas.add(var,van))
		elif choice ==2:
			print(f"Substraction of {var} - {van} is..")
			print(objectas.sub(var,van))
		elif choice == 3:
			print(f"Multiplication of {var} and {van} is....")
			print(objectas.mul(var, van))
		elif choice == 4:
			print(f"Division of {var} / {van} is..")
			print(objectas.div(var,van))
		else:
			#print("thank you")
			break
		#print("I'm outside the loop, thanks for using the calci")


def main():
	objectas = MyClass()
	objectas.operation()


if __name__ == "__main__":
	main()











