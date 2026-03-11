s = open('24.txt').read().strip()

idxes = [i for i in range(len(s)) if s[i] == 'A']
pod = []
for i in range(2, len(idxes)):
    pod.append(idxes[i] - idxes[i-2] + 1)
print(max(pod))

# 501
