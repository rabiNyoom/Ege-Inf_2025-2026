# 24764
cmd_map = {
    (' ', 0): ('1', 1, 1),
    (' ', 1): ('2', 1, 2),
    (' ', 2): ('3', None, 0),

    ('0', 0): ('0', 1, 1),
    ('0', 1): ('1', 1, 2),
    ('0', 2): ('3', 1, 0),

    ('1', 0): ('0', 1, 1),
    ('1', 1): ('1', 1, 2),
    ('1', 2): ('3', 1, 0),
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


s = '01' * 500
r = tm(s)

print(sum(map(int, r)))
