import sys
import sqlite3

def countChars(text, character):
	char_sum = 0
	for char in text:
		if char == character:
			char_sum += 1
	
	return char_sum

# checks if a string's character matches a set of characters
# in a specific order
# a list of characters should be passed to the "characters" argument
def charMatch(text, characters):
	pass
	# work on it later, I want to get something to work first

def charsExist(text, characters):
	char_found = True # this is done to make sure that it returns true if no characters were passed
	for character in characters:
		char_found = False
		for letter in text:
			if letter == character:
				char_found = True
				break
		if char_found:
			continue
		else:
			break
	
	return char_found

def initDB():
	# vars
	database_path = "words"

	# create/connect to database
	db = sqlite3.connect(database_path)

	# creating cursor in-order to execute SQL on the database
	cursor = db.cursor()
	
	# create the "words" table if it wasn't already created
	cursor.execute('''
		CREATE TABLE IF NOT EXISTS words(word TEXT PRIMARY KEY, length INTEGER, spaces INTEGER)
	''')
	
	# commit changes to database
	db.commit()
	
	# toss the cooked database to the user
	return db

# adds a word to the "words" database. Will return "True" or "False" based
# on whether or not it's successful(the word might already be in the database)
def addWord(db, word):
	# getting word stats
	length = len(word)
	spaces = countChars(word, " ")

	try:
		# inserting data into database
		cursor = db.cursor()
		cursor.execute('''
			INSERT INTO words(word, length, spaces)
			VALUES ('{0}', {1}, {2})	
		'''.format(word, length, spaces))
		
		# comitting changes to database
		db.commit()
		
		return True
	except:
		return False

# remove a word from the database
# returns True or False based on whether or not the removal
# was successsful(might not even be in the database)
def removeWord(db, word):
	try: 
		cursor = db.cursor()
		cursor.execute('''
			DELETE FROM words WHERE word = '{0}'
		'''.format(word))

		db.commit()

		return True
	except:
		return False

# the "characters" argument requires a list of words, which
# could be useful in-case some words were already revealed
def findWords(db, length, spaces, characters=[]):
	cursor = db.cursor()
	cursor.execute('''
		SELECT word
		FROM words
		WHERE length = {0} AND spaces = {1}
	'''.format(length, spaces))

	words = cursor.fetchall()
	filtered_words = []
	for item in words:
		word = item[0]
		if charsExist(word, characters):
			filtered_words.append(word)

	return filtered_words

def main(args):
	if len(args) == 1:
		print("Usage:")
		print("{0} search <length> <spaces> [characters...]".format(args[0]))
		print("{0} add <word>".format(args[0]))
		print("{0} remove <word>".format(args[0]))
	elif args[1] == "search":
		length = args[2]
		spaces = 0
		if len(args) > 3:
			spaces = args[3]
		characters = []
		if len(args) > 4:
			for i in range(4, len(args)):
				char = args[i]
				characters.append(char)

		print("Search criteria:")
		print("length: {0}\nspaces: {1}\ncharacters: {2}\n".format(length, spaces, characters))
		
		db = initDB()

		found_words = findWords(db, length, spaces, characters)

		db.close()

		if len(found_words) > 0:
			found_words.sort()
			print("Here's a list of matching words:")
			for word in found_words:
				print("	{}".format(word))
		else:
			print("No words matched the search criteria!")	
	elif args[1] == "add":
		word = args[2]
		
		db = initDB()
		
		worked = addWord(db, word)
		
		db.close()

		if worked:
			print("The word '{}' was successfully entered into the database!".format(word))
		else:
			print("Unable to enter '{}' into the database, the word might already be there!".format(word))
	elif args[1] == "remove":
		word = args[2]

		db = initDB()
		
		worked = removeWord(db, word)
		
		db.close()

		if worked:
			print("The word '{}' was successfully removed from the database!".format(word))
		else:
			print("Unable to remove {}, it might not be in the database!".format(word))
	else:
		print("Invalid arguments!")

if __name__ == "__main__":
	main(sys.argv)
