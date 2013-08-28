
def options():
	#choice of calculator functions
	print "Choose an operator \n"
	print "1: Addition"
	print "2: Subtraction"
	print "3: Multiplication"
	print "4: Division"
	print "4: Quit"

	#return input("Choose your operator: " )

#swag
def add(x):
	return "The sum is: ",sum(x)
	
def divide(x,y):
	return x/y
#def multiply(i, j):
	#return i *j

def main():
	options()
	selec = 0
	while True:
		selec = int(raw_input("Select the corresponding number for operator: "))
		if selec == 1: 
			prompt = raw_input("Enter a sequence of numbers SEPARATED BY SPACES to add: ").split()
			print prompt
			nums = []
			for x in prompt:
				nums.append(int(x))
			#print nums
			print add(nums)

		elif selec == 2:
			prompt = input("Select two numbers to subtract from one another: ")
			print prompt
			


main()