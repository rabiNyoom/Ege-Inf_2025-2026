L = -1; S = 2
progs = {
    (' ', 0): (' ', L, 2),
    (' ', 1): (' ', S, 2),
    (' ', 2): (' ', S, 1),
    
    ('0', 1): ('1', S, 2),
    ('0', 2): (' ', L, 1),
    
    ('1', 1): (' ', L, 2),
    ('1', 2): (' ', L, 1),
}

def tm(n):
    s = list(' ' + n + ' ')
    i = len(s)-1
    q = 0
    while True:
        char, mov, state = progs[s[i], q]
        s[i] = char
        if mov == S:
            break
        i += mov
        q = state
    return ''.join(s)

s = f'{21418:b}'
print(int(tm(s), 2))