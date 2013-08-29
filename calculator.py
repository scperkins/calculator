
def options():
	#choice of calculator functions
	print "Choose an operator \n"
	print "1: Addition"
	print "2: Subtraction"
	print "3: Multiplication"
	print "4: Division"
	print "5: Modulo"
	print "6: Quit"

	#return input("Choose your operator: " )

#swag
#now not so much. #yolo anyway
def add(x):
	return "The sum is: ",sum(x)

def subtr(x):
	return x[0]-x[1]
	
def divide(x):
	if x[1] == 0:
		print "Good job. You just destroyed the universe."
	else: return x[0]/x[1]

def mult(x):
	return x[0]*x[1]

def mod(x):
	return x[0] % x[1]


def main():
	options()
	selec = 0
	while True:
		selec = int(raw_input("Select the corresponding number for operation: "))
		if selec == 1:
			#some ugly, dirty code, but it demonstrates a few things 
			prompt = raw_input("Enter a sequence of numbers SEPARATED BY SPACES to add: ").split()
			print prompt
			nums = []
			for x in prompt:
				nums.append(float(x))
			#print nums
			print add(nums)

		elif selec == 2:
			prompt = raw_input("Enter a sequence of numbers SEPARATED BY SPACES to be subtracted from each other: ").split()
			nums = []
			for x in prompt:
				nums.append(float(x))
			print subtr(nums)

		elif selec == 3:
			prompt = raw_input("Enter a sequence of numnbers, SEPARATED BY SPACES you wish to multiply: ").split()
			nums = []
			for x in prompt:
				nums.append(float(x))
			print mult(nums)

		elif selec == 4:
			prompt = raw_input("Select two numbers SEPARATED BY SPACES to divide from one another: ").split()
			nums = []
			for x in prompt:
				nums.append(float(x))
			print divide(nums)

		elif selec == 5:
			prompt = raw_input("Enter two numbers SEPARATED BY SPACES to be modded: ").split()
			nums = []
			for x in prompt:
				nums.append(int(x))
			print mod(nums)

		elif selec == 6:
			return False

main()