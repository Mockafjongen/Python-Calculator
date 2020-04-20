num3 = 0

print("---" * 9)
print("What is the code?")
lock = input()

if lock == "1234":
	print("---" * 9)
	print("Do you want info about the calculator or do you want to calculate something?")
	choice = input()
	
	if choice == "info" or choice == "i":
		print("This is a basic calculator made by Felix Lindgren. You can calculate up to 3 numbers right now and it has support for +, -, * and /.")
	
	if choice == "calculate" or choice == "c":
		print("How many numbers do you want to calculate?")
		nums = input()
		
		if nums == "2":
			print("What is the first number?")
			num1 = input()
			print("What is the second number?")
			num2 = input()
  	
		if nums == "3":
			print("What is the first number?")
			num1 = input()
			print("What is the second number?")
			num2 = input()
			print("What is the third number?")
			num3 = input()
  		
		print("What operator do you want to use?")
		operator = input()
		print("---" * 9)
  	
		if operator == "+":
			print("The answer is " + str(int(num1) + int(num2) + int(num3)))
		elif operator == "-":
			print("The answer is " + str(int(num1) - int(num2) - int(num3)))
		elif operator == "*":
			print("The answer is " + str(int(num1) * int(num2) * int(num3)))
		elif operator == "/":
			print("The answer is " + str(int(num1) / int(num2) / int(num3)))
		else:
			print("Thats not an operator.")
		print("---" * 9)

if lock != "1234":
	print("---" * 9)
	print("Wrong passcode!")
	print("---" * 9)
