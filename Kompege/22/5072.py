proc = {}
for l in open('5072.txt'):
    s = l.split()
    pid, base, deps = int(s[0]), int(s[1]), list(map(int, s[2].split(';')))
    proc[pid] = {'base': base, 'deps': deps,
                 'time': base if deps == [0] else None}

while any(p['time'] is None for p in proc.values()):
    for p, v in proc.items():
        if v['time'] is None:
            times = []
            for d in v['deps']:
                times.append(proc[d]['time'])
            if None not in times:
                proc[p]['time'] = v['base'] + max(times) + 7

print(max(v['time'] for v in proc.values()))
