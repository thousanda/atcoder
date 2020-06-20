# しゃくとり法
'''
len(a) = N
print(num), where num = count sum(partial_seq(a)) >= K
4 10
6 1 2 7
'''

N = 4
K = 10
a = [6, 1, 2, 7]

interval = 0
ans = 0
left = 0
right = 0
print(a)
while True:
    print(f'{left=}, {right=}, {interval=}', end=' ')
    if interval < K:
        if right == N:
            print()
            break
        interval += a[right]
        right += 1
    else:
        ans += N - right + 1
        print(f'ans += {N-right+1}', end='')
        interval -= a[left]
        left += 1
    print()
print(ans)
