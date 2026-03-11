L = -1
S = 2
progs = {
    (' ', 0): (' ', L, 1),
    (' ', 2): (' ', S, 2),
    (' ', 3): (' ', S, 3),

    ('1', 1): ('1', L, 2),
    ('1', 2): ('0', L, 3),
    ('1', 3): ('1', L, 2),

    ('0', 1): ('0', L, 3),
    ('0', 2): ('1', L, 2),
    ('0', 3): ('0', L, 3),
}


def tm(n):
    s = list(' ' + n + ' ')
    i = len(s) - 1
    q = 0

    while True:
        char, mov, state = progs[s[i], q]
        s[i] = char
        if mov == S:
            break
        i += mov
        q = state

    return ''.join(s)


s = '0' * 100
r = tm(s)
print(r.count('0'))

# 100
