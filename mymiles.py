# Ask the user to input 2 Values and store them in variables
num1 = input('Enter Miles ')
# Convert the strings into Float numbers Integer
num1 = float(num1)
# convert the values entered and store in Kilometers
kilometers = num1 * 1.60934
# Print the result
print("{} miles equals {} Kilometers".format(num1, kilometers))