def f(s, m):
    if s >= 229:
        return m % 2 == 0
    if m == 0:
        return 0
    mov = [f(s+1, m-1), f(s*2, m-1)]
    return all(mov) if m % 2 == 0 else any(mov)


print('19:', *[s for s in range(1, 229) if f(s, 2)])
print('20:', *[s for s in range(1, 229) if f(s, 3)])
print('21:', *[s for s in range(1, 229) if not f(s, 2) and f(s, 4)])

# 114
# 57 113
# 112
