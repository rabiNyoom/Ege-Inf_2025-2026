# 25239
cmd_map = {
    (' ', 0): (' ', -1, 1),
    (' ', 1): (' ', None, 1),
    (' ', 2): (' ', None, 1),

    ('1', 1): ('0', None, 2),
    ('1', 2): ('1', -1, 1),

    ('0', 1): ('1', -1, 2),
    ('0', 2): ('0', -1, 1),
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


base = f'{32768:b}'
for i in range(1000, 0, -1):
    n = '0' * i + base
    r = tm(n)
    if r.count('0') == 200:
        print(n.count('0'))
        break
