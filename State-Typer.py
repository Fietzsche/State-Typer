file = open("statelist.txt", "r")
statelist = file.readlines()
stateFound = False
remainingStates = 50
usedStates = []

while remainingStates > 0:
	text = input("Enter a state\n")

	# Checks the state list file to see if the user input matches any of the states listed
	for state in statelist:
		if text.lower() == "canada":
			remainingStates = 0
		if text.lower() in state and text.lower() not in usedStates:
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
	elif stateFound == False and state in statelist:
		print("Sorry, " + text + " is not recognized as a state.\n")

print("Congratulations! That's all the states!")