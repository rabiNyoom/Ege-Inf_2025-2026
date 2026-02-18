from itertools import permutations
c = 0
for p in permutations('АБИКОЛУН'):
    s = ''.join(p)
    s = s.replace('А', 'g').replace('И', 'g').replace('О', 'g').replace(
        'У', 'g').replace('Б', 's').replace('К', 's').replace('Л', 's').replace('Н', 's')
    if 'ss' not in s and 'gg' not in s:
        c += 1
print(c)
