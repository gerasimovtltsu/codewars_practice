def next_bigger(n):
    s = str(n)
    for i in range(len(s) - 2, -1, -1):
        if s[i] < s[i + 1]:
            for k in range(len(s) - 1, i, -1):
                if s[i] < s[k]:
                    return int(s[:i] + s[k] + s[-1:k:-1] + s[i] + s[k - 1:i:-1])
    else:
        return -1

print(next_bigger(12))