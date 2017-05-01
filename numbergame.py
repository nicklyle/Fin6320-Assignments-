from random import randint

def main():

def computer_guesses(number):
	lowerbound = 1
	upperbound = 100
	guess = randint(1,100)
	while guess != number:
		print("Hmm, is your number",guess?)
		if guess > number:
			high = guess 
		elif guess < number:
			low = guess + 1
		guess = (low+high)//2

	print("I got it! your number is",guess)

number = int(input("Please Select a number: "))
	
if __name__ == "__main__":
	main()
