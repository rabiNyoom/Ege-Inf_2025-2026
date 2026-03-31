file = '4791.txt'
proc = {}
for l in open(file):
    s = l.split()
    pid, base_time, deps = int(s[0]), int(
        s[1]), list(map(int, s[2].split(';')))
    proc[pid] = {'time': base_time if deps == [0]
                 else None, 'base': base_time, 'deps': deps}

while any(v['time'] is None for v in proc.values()):
    for pid, data in proc.items():
        if data['time'] is None:
            times = []
            for d in data['deps']:
                times.append(proc[d]['time'])
            if None not in times:
                proc[pid]['time'] = data['base'] + max(times)
print(max(v['time'] for v in proc.values()))
