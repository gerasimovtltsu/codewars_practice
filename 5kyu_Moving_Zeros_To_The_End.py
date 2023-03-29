def move_zeros(lst):
    return sorted(lst, key=lambda x: not x)

print(move_zeros([1, 0, 1, 2, 0, 1, 3])) # returns [1, 1, 2, 1, 3, 0, 0]