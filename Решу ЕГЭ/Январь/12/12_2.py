# 25293
cmd_map = {
    (' ', 0): (' ', 1, 1),
    (' ', 1): (' ', None, 1),

    ('0', 1): ('1', None, 1),

    ('1', 1): ('0', 1, 1),
}


def tm(n: str) -> str:
    s = list(' ' + n + ' ')
    i = 0
    q = 0

    while True:
        char, mov, state = cmd_map[s[i], q]
        s[i] = char
        if mov is None:
            break
        i += mov
        q = state

    return ''.join(s)


for i in range(0, 600):
    n = '0' * (600-i) + '1' * i
    r = tm(n)
    if r.count('0') == 250:
        print(i)
        break
