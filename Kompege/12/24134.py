L, S = -1, 2
cmds = {
    (" ", 0): (" ", L, 1),
    (" ", 1): (" ", S, 1),
    ("1", 0): ("0", L, 0),
    ("1", 1): ("0", L, 0),
    ("0", 0): ("0", L, 1),
    ("0", 1): ("1", L, 1),
}


def tm(n):
    s = list(" " + n + " ")
    q = 0
    i = len(s) - 1
    while True:
        char, mov, state = cmds[s[i], q]
        s[i] = char
        if mov == S:
            break
        i += mov
        q = state
    return "".join(s)


s = "0" * 900 + "10" * 50
assert tm(s).count("0") == 100
print(s.count("0"))
