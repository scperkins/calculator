
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
#now not so much. #yolo anyway
def add(x):
	return "The sum is: ",sum(x)
	
def divide(x):
	return x[0]/x[1]

def mult(i):
	return i[0]*i[1]

def main():
	options()
	selec = 0
	while True:
		selec = int(raw_input("Select the corresponding number for operation: "))
		if selec == 1: 
			prompt = raw_input("Enter a sequence of numbers SEPARATED BY SPACES to add: ").split()
			print prompt
			nums = []
			for x in prompt:
				nums.append(float(x))
			#print nums
			print add(nums)

		elif selec == 4:
			prompt = raw_input("Select two numbers to divide from one another: ").split()
			nums = []
			for x in prompt:
				nums.append(float(x))
			print divide(nums)
			#print divide(prompt)

		elif selec == 3:
			prompt = raw_input("Enter a sequence of numnbers, SEPARATED BY SPACES you wish to multiply: ").split()
			nums = []
			for x in prompt:
				nums.append(float(x))
			print mult(nums)




main()