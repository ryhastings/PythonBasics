# firstmodule.py

def addition(x, y):
	print("Add")
	c = x + y
	print("{} + {} = {}".format(x,y,c))
	return

def subtraction(x, y):
	print("Subtract")
	c = x - y
	print("{} - {} = {}".format(x, y, c))
	return

def addsubtract(x,y,symbol):
	if symbol == "+":
		c = x + y
	elif symbol == "-":
		c = x - y
	else:
		c = unrecognized
	return c

if __name__ == "__main__":
	x = input("input a command: ")
	print("You entered {}.".format(x))
	a = int(input("a = "))
	b = int(input("b = "))
	if x == 'add' or x == 'a':
		symbol = "+"
		answer = addsubtract(a,b,symbol)
	elif x == "s" or s == 'subtract':
		symbol = "-"
		answer = addsubtract(a,b,symbol)
	else:
		print("{} not recognized".format(x))
		print("Enter a new command")
	print("c = {}.".format(answer))
	print("Done")