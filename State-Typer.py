file = open("statelist.txt", "r")
statelist = file.readlines()
stateFound = False
remainingStates = 50
usedStates = []

while remainingStates > 0:
	text = input("Enter a state\n")

	# Checks the state list file to see if the user input matches any of the states listed
	for state in statelist:
		if text.lower() in state and text.lower() not in usedStates and len(text + "\n") is len(state):
			stateFound = True
			remainingStates -= 1
			usedStates.append(text.lower())
			break
		elif text.lower() in usedStates:
			print ("You've already said " + text.lower() + ".\n")
			break

	if stateFound == True:
		print("Correct\n")
		print("There are " + str(remainingStates) + " states left.\n")
		stateFound = False
	elif stateFound == False and text.lower() not in usedStates:
		print("Sorry, " + text + " is not recognized as a state.\n")

print("Congratulations! That's all the states!")
