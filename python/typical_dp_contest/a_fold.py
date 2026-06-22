import functools

N = int(input())
ps = list(map(int, input().split()))

def apply(acc: set[int], curr: int):
    new_nums = [n + curr for n in acc]
    return acc.union(new_nums)

def solve(ps):
    nums = functools.reduce(apply, ps, set([0]))
    return len(nums)

print(solve(ps))

# 1行で書くとこう
# print(len(functools.reduce(lambda acc, curr: acc.union([n+curr for n in acc]), ps, set([0]))))
