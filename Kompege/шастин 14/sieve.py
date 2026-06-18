n = 6_000_000
a = [True] * (n + 1)
a[0] = False
a[1] = False
for i in range(2, n + 1):
    if a[i]:
        for j in range(i * i, n + 1, i):
            a[j] = False
s = [str(i) for i in range(n + 1) if a[i] and str(i).count("2") == 1]
with open("out.txt", "w") as f:
    f.write(" ".join(s))
print("Done")
