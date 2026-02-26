def f(s, m):
    if s <= 60:
        return m % 2 == 0
    if m == 0:
        return 0

    mov = [f(s-3, m-1), f(s-5, m-1), f(s//4, m-1)]

    return all(mov) if m % 2 == 0 else any(mov)


print('19:', min([s for s in range(61, 1000) if not f(s, 1) and f(s, 2)]))
print('20:', *[s for s in range(61, 1000)
      if not f(s, 1) and not f(s, 2) and f(s, 3)][:2])
print('21:', min([s for s in range(61, 1000) if not f(s, 2) and f(s, 4)]))

# 244
# 247 248
# 252
