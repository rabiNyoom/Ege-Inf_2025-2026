# 25292
cmd_map = {
    (' ', 0): (' ', -1, 1),
    (' ', 1): (' ', None, 1),

    ('0', 1): ('1', -1, 1),

    ('1', 1): ('0', None, 1),
}


def tm(n: str) -> str:
    s = list(' ' + n + ' ')
    i = len(s) - 1
    q = 0

    while True:
        char, mov, state = cmd_map[s[i], q]
        s[i] = char
        if mov is None:
            break
        i += mov
        q = state

    return ''.join(s)


for i in range(1000, 0, -1):
    n = '0' * (1000 - i) + '1' * i
    r = tm(n)
    if r.count('0') == 200:
        print(i)
        break
