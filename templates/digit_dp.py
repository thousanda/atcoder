
# N以下の非負整数 (一番左の数が0でもOK) の数を数える
'''
N = 8357 のとき

0??? ~ 7???
80?? ~ 82??
830? ~ 834?
8350 ~ 8356
8357
'''

N = '8357'

num = [0, 0, 0, 0]

for i, d in enumerate(str(N)):
    e = len(N) - i - 1  # 10の何乗か
    print(f'{i=}, {d=}, {e=}')
    num[i] = int(d) * (10**e)

print(num)
print(f'The number of non-negative integers less than or equal to {N} = {sum(num)+1}')
