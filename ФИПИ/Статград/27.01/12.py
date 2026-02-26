R = 1
S = 2
progs = {
    (' ', 0): ('1', R, 1),
    (' ', 1): ('0', R, 2),
    (' ', 2): ('0', R, 3),
    (' ', 3): ('1', S, 3),

    ('0', 1): ('0', R, 1),

    ('1', 1): ('1', R, 1),
}


def tm(n):
    s = list(' ' + n + '       ')
    i = 0
    q = 0

    while True:
        char, mov, state = progs[s[i], q]
        s[i] = char
        if mov == S:
            break
        i += mov
        q = state
    return ''.join(s)


n = f'{145682:b}'
print(int(tm(n), 2))

# 3262609
