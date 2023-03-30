def get_length_of_missing_array(array_of_arrays):
    lengths = [len(a) if a is not None else 0 for a in array_of_arrays]
    lengths.sort()
    if 0 in lengths or len(lengths) == 0:
        return 0
    for i in range(len(lengths)):
        if lengths[i + 1] != lengths[i] + 1:
            return lengths[i] + 1


print(get_length_of_missing_array(
    [[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]]))
