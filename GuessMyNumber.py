import random

def validGuess(entry, min, max):
	if entry.isdigit() and min <= int(entry) <= max:
		return True
	else:
		return False

def main():
	print("\n\n********        Guess My Number        ********\n")
	userMin = int(input("Input your minimum number: "))
	userMax = int(input("Input your maximum number: "))
	print("Your minimum is %s and your maximum is %s.\n\nLet's begin!\n" % (userMin, userMax))
	
	number = random.randint(userMin,userMax)
	numberOfGuesses = 0
	correctGuess = False
	userGuess = input("Input a number between %s and %s: " % (userMin, userMax))
	
	while not correctGuess:
		if not validGuess(userGuess, userMin, userMax):
			userGuess = input("Not a valid guess. Use a number between %s and %s: " % (userMin, userMax))
			continue
		else:
			numberOfGuesses += 1
			userGuess = int(userGuess)
		
		if userGuess < number:
			userGuess = input("That's too low. Try again: ")
		elif userGuess > number:
			userGuess = input("That's too high. Try again: ")
		else:
			print("You guessed correctly in %s guesses!" % (numberOfGuesses))
			correctGuess = True
	print("\n\n****        GAME OVER        ****\n\n")
	
main()