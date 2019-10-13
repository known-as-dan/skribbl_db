import sys
import re
import json

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

cached_words = {}
modified = True
def getWords():
	global modified
	global cached_words

	if modified:
		file_obj = open("words.js", "r")
		file_content = file_obj.read()

		search_result = re.search("\\{.*\\}", file_content, flags=re.S)
		words_json = search_result.group()
		words = json.loads(words_json)

		modified = False
		cached_words = words
		return words
	else:
		return cached_words

def setWords(words):
	words_json = json.dumps(words, indent=4)

	file_obj = open("words.js", "w")
	file_obj.write("var words = " + words_json)

	global modified
	modified = True

# adds a word to the "words" database. Will return "True" or "False" based
# on whether or not it's successful(the word might already be in the database)
def addWord(word):
	# setting all word characters to lowercase characters
	word = word.lower()
	
	# getting word stats
	spaces = countChars(word, " ")
	length = len(word) - spaces

	words = getWords()
	try:
		words[word]
		return False
	except:
		words[word] = {
			"length": length,
			"spaces": spaces
		}
		setWords(words)

		return True

# remove a word from the database
# returns True or False based on whether or not the removal
# was successsful(might not even be in the database)
def removeWord(word):
	word = word.lower()
	words = getWords()
	try:
		words[word]
		words.pop(word)
		setWords(words)
		
		return True
	except:
		return False

# the "characters" argument requires a list of words, which
# could be useful in-case some words were already revealed
def findWords(length, spaces=0, characters=[]):
	words = getWords()
	filtered_words = []
	for word in words:
		word_obj = words[word]
		word_length = word_obj["length"]
		word_spaces = word_obj["spaces"]
		if word_length == length and word_spaces == spaces and charsExist(word, characters):
			filtered_words.append(word)

	return filtered_words