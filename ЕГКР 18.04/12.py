R = 1
S = 2
cmds = {
    (' ', 0): (' ', R, 1),
    (' ', 1): ('1', R, 2),
    (' ', 2): ('1', R, 3),
    (' ', 3): (' ', S, 3),

    ('0', 1): ('0', R, 1),

    ('1', 1): ('1', R, 1),
}


def tm(n):
    s = list(' ' + n + '   ')
    i = 0
    q = 0
    while True:
        char, mov, state = cmds[s[i], q]
        s[i] = char
        if mov == S:
            break
        i += mov
        q = state
    return ''.join(s)


n = f'{2027:b}'
r = int(tm(n), 2)
print(r)
