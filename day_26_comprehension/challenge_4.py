# Supposed to print a dictionary that has the words in the string below as a list and their lengths as the values.
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
sentence_list = sentence.split()
result = {word:len(word) for word in sentence_list}


print(result)