import skdb
from command import command
from command import utilities

def search(args):
	length = int(utilities.isArg(args, 0, default="0"))
	spaces = int(utilities.isArg(args, 1, default="0"))
	if len(args) > 2:
		characters = args[2:]
		characters = list(map(lambda char: char.lower(), characters))
	else:
		characters = []

	separator = "────────────────────────────────────────"
	print(separator)
	print("Search criteria:")
	print("length: {0}\nspaces: {1}\ncharacters: {2}".format(length, spaces, characters))
	print(separator)

	found_words = skdb.findWords(length, spaces, characters)

	if len(found_words) > 0:
		found_words.sort()
		print("Matching word(s):")
		for i in range(len(found_words)):
			word = found_words[i]
			print("{0}. {1}".format((i + 1), word))
	else:
		print("No words matched the search criteria!")
	
	print(separator)

command.Command("search", "<length> <spaces> [characters...]", "Search for words that match a certain criteria.", search)

def add(args):
	word = utilities.isArg(args, 0)
	if word:
		worked = skdb.addWord(word)
		if worked:
			print("The word '{}' was successfully entered into the database!".format(word))
		else:
			print("Unable to enter '{}' into the database, the word might already be there!".format(word))
	else:
		print("Please enter a word to add!")

command.Command("add", "<word>", "Add a word to the database.", add)

def remove(args):
	word = utilities.isArg(args, 0)
	if word:
		worked = skdb.removeWord(word)
		if worked:
			print("The word '{}' was successfully removed from the database!".format(word))
		else:
			print("Unable to remove {}, it might not be in the database!".format(word))
	else:
		print("Please enter a word to remove!")

command.Command("remove", "<word>", "Remove a word from the database.", remove)

command.init()