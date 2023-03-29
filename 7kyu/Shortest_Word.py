"""
Simple, given a string of words, return the length of the shortest word(s).
String will never be empty and you do not need to account for different data types.
"""

def find_short(s):
	words = s.split()
	l = len(min(words, key=len))
	return l # l: shortest word length

print(find_short("bitcoin take over the world maybe who knows perhaps"))