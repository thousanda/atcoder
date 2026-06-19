N = int(input())
ps = list(map(int, input().split()))

def solve(ps):
    nums = set([0])
    for p in ps:
        for num in nums.copy():
            nums.add(num + p)
    return len(nums)

print(solve(ps))
