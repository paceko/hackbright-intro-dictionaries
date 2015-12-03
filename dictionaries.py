#my_stats = {"name": "patricia", "age": 30, "height": 5.8}
#print "%s is %i years old with a height of %.2f." %(my_stats["name"], my_stats["age"], my_stats["height"])

#del(my_stats["age"])
#print my_stats

#vocabulary_words = {"float": "decimal number", "string": "anything between parantheses", "integer": "any whole number", "boolean": "True or False"}

# my_name = "patricia"
# letter_count = {}

# for letter in my_name:
# 	if letter in letter_count:
# 		letter_count[letter] += 1
# 	else:
# 		letter_count[letter] = 1

# print letter_count

file_monday = open("one_fish_two_fish.txt").read()
letter_count = {}

for letter in file_monday:
	if letter in letter_count:
		letter_count[letter] += 1
	else:
		letter_count[letter] = 1

print letter_count

# my_name = "one fish two fish red fish blue fish"
# letter_count = {}

# for letter in my_name:
# 	if letter in letter_count:
# 		letter_count[letter] += 1
# 	else:
# 		letter_count[letter] = 1

# print letter_count

# prices = {}


# my_fruit = {"banana": 4, "apples": 2, "orange": 1.5, "pear": 3} 
# max = 0
# max_key = ""
# for key, value in my_fruit.items():
#     if 

# print max_key

