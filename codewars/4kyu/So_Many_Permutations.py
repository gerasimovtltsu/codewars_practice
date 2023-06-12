'''
In this kata, your task is to create all permutations of a non-empty input string and remove duplicates, if present.

Create as many "shufflings" as you can!

Examples:

With input 'a':
Your function should return: ['a']

With input 'ab':
Your function should return ['ab', 'ba']

With input 'abc':
Your function should return ['abc','acb','bac','bca','cab','cba']

With input 'aabb':
Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

Нужно использовать алгоритм скользящего окна
'''

def permutations(string: str):
	res = set([string])
	if len(string) == 2:
		res.add(string[1] + string[0])
	elif len(string) > 2:
		for i, char in enumerate(string):
			for s in permutations(string[:i] + string[i + 1:]):
				res.add(char + s)

	return list(res)


print(permutations('ab'))