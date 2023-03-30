def sum_strings(x, y):
    x,y = map(str.strip, (x,y))

    if (x == '0' and y =='0') or (x == '' and y == ''):
        return "0"
    
    maxLen = max(len(x), len(y))

    x = x.zfill(maxLen)[::-1]
    y = y.zfill(maxLen)[::-1]

    r = []
    carryover = 0

    for i  in range(maxLen):
        carryover, res = str(int(x[i]) + int(y[i]) + int(carryover)).zfill(2)
        r.append(res)
        if i == maxLen-1:
            r.append(carryover)
    r = "".join(r)[::-1].lstrip("0")
    return r if r else "0"