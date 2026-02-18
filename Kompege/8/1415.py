from itertools import product
cnt = 0
for p in product('123AB', repeat=8):
    dgts = 0
    for c in p:
        if c.isdigit():
            dgts += 1
    if dgts == 6:
        cnt += 1
print(cnt)
