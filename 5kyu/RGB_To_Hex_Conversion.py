def rgb(r, g, b):
    rnd = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(rnd(r), rnd(g), rnd(b))