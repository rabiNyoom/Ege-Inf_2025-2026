R = 1
L = -1
S = 2
cmds = {
    (" ", 0): (" ", R, 1),
    (" ", 1): (" ", L, 2),
    ("0", 1): ("0", R, 1),
    ("0", 2): (" ", L, 3),
    ("0", 3): (" ", S, 3),
    ("1", 1): ("1", R, 1),
    ("1", 2): (" ", L, 3),
    ("1", 3): ("1", S, 3),
}


def tm(n):
    s = list(" " + n + " ")
    i = 0
    q = 0
    while True:
        char, mov, state = cmds[s[i], q]
        s[i] = char
        if mov == S:
            break
        i += mov
        q = state
    return "".join(s)


s = f"{1097:b}"
print(int(tm(s), 2))
