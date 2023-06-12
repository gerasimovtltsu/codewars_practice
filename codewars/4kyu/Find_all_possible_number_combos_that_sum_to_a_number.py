"""
4 kyu
Find all possible number combos that sum to a number
https://www.codewars.com/kata/555b1890a75b930e63000023/train/python
"""

def combos(n) -> list:
    if n:
        for sub in combos(n - 1):
            yield [1] + sub
            if sub and (len(sub) < 2 or sub[1] > sub[0]):
                yield [sub[0] + 1] + sub[1:]
    else:
        yield []