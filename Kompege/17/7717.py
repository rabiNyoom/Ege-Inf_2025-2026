nums = [int(l) for l in open('7717.txt')]
c = m = 0


def fn(n):
    s = list(str(n))
    if len([d for d in s if d in ['0', '2', '4', '6', '8']]) == len([d for d in s if d in ['1', '3', '5', '7', '9']]):
        return True
    return False


def compare(a, b):
    s1, s2 = sorted(list(str(a))), sorted(list(str(b)))
    if int(s2[-1]) < int(s1[0]):
        return True
    return False


maxi = max(filter(fn, nums))
c = m = 0
for a, b in zip(nums, nums[1:]):
    if compare(a, b) and (a + b) <= maxi:
        c += 1
        m = max(m, a + b)
print(c, m)
