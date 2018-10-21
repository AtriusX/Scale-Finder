# The Ionian note index
key_values = [0, 2, 4, 5, 7, 9, 11]
# All modes
modes = ["ionian", "dorian", "phrygian", "lydian", "mixolydian", "aeolian", "locrian"]
# All Keys
keys = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
# Rotate the elements of a list around
def rotate(lst, x):
    lst[:] =  lst[-x:] + lst[:-x]

# Shifts and wraps values in a list to a specified range
def wrap(shift, low, high, list):
	for i in range(0, len(list)):
		list[i] += shift
		if (list[i] > high):
			list[i] = list[i] - high - (i == len(list) if 0 else 1)
		elif (list[i] < low):
			list[i] = high + list[i] + (i == len(list) if 0 else 1)

# Shift the input down to a specific value
def shift(list, item):
	shift = list[0] - keys.index(item)
	wrap(-shift, 0, 11, list)

# Find the scale for the given input
def find_scale(input):
	# Split the input
	values = input.split(" ")
	try:
		key, mode = values
		local_spacings = key_values.copy()
		
		# Rotate the list to change the root key
		rotate(local_spacings, -modes.index(mode.lower()))
		
		# Shift the entire list down to the proper key
		shift(local_spacings, key.capitalize())

		# Read out the proper values
		print("Keys for " + input + ":", end =" ")
		for i in range(0, len(local_spacings)):
			print(keys[local_spacings[i]], end = " ")
		print("\n")
	except(Exception):
		# Return an error if input is incorrect
		print("Required format: <key> <mode> | <key|mode> all | all")

# User Input	
while(True):
	print("Enter a scale and mode or type 'Exit':", end = " ")
	text = input()

	# Exit program
	if (text.lower() == "exit"):
		break
	
	# Display all values for a key
	split = text.split()
	if (text.lower().endswith("all") and len(split) < 3):
		
		# Return all modes for a key
		if (split[0].capitalize() in keys):
			print("Modes for key:")
			for i in modes:
				find_scale(split[0] + " " + i)

		# Return all keys for a mode
		elif (split[0].lower() in modes):
			print("Keys for mode:")
			for i in keys:
				find_scale(i + " " + split[0])

	# Display every scale
	if (text.lower() == "all"):
		for key in keys:
			for mode in modes:
				find_scale(key + " " + mode)
			print("------------------------------------")

	find_scale(text)
