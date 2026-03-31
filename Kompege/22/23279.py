proc = {}
for l in open('23279.txt'):
    s = l.split()
    pid, base, deps = int(s[0]), int(s[1]), list(map(int, s[2].split(';')))
    proc[pid] = {'base': base, 'deps': deps, 'start': 0 if deps ==
                 [0] else None, 'end': base if deps == [0] else None}

while any(p['end'] is None for p in proc.values()):
    for p, v in proc.items():
        if v['end'] is None:
            times = []
            for d in v['deps']:
                times.append(proc[d]['end'])
            if None not in times:
                proc[p]['start'] = max(times)
                proc[p]['end'] = v['base'] + max(times)

for t in range(1, 50):
    if len([1 for v in proc.values() if v['end'] <= t]) >= 14:
        print(t)
        break
