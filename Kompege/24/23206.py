import re

with open("23206.txt", "r") as f:
    s = f.read().strip()

max_len = 0

for match in re.finditer(r"[02468][^02468]*", s):
    block = match.group()
    start = match.start()
    print(block)

    count = 0
    for i, ch in enumerate(block):
        if ch == "S":
            count += 1
            if count == 36:
                if i > max_len:
                    max_len = i
                break

print(max_len)
