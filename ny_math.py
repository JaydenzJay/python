def calculate(op1, op2, f):
	if f == "add":
		return op1 + op2
	elif f == "subtract":
		return op1 - op2 
	elif f == "divide":
		return op1 / op2
	elif f == "multiply":
		return op1 * op2
	
print("Select Options")
print("Add")
print("Subtract")
print("Multiply")
print("Divide")
option = raw_input("Enter your Option" )

op1 = int(raw_input("Enter your first number" ))

op2 = int(raw_input("Enter your second number" ))

results = calculate(op1, op2, option)
print results
   
