# basics.py

x = input("input a command: ")
print("You entered {}.".format(x))
if x == 'add' or x == 'a':
	print("Add")
	a = 1
	b = 2
	c = a + b
	print("{} + {} = {}".format(a,b,c))
elif x == "s" or s == 'subtract':
	print("Subtract")
	a = 1
	b = 2
	c = a - b
	print("{} - {} = {}".format(a, b, c))
else:
	print("{} not recognized".format(x))
print("Done")