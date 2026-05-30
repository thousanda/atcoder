import functools
import numpy as np
import sys

abc = np.loadtxt(sys.stdin, dtype=int, skiprows=1, ndmin=2)

def apply(acc: np.ndarray, next: np.ndarray) -> np.ndarray:
    """max-plus代数における畳み込み where i != j

    :param acc これまでの累積幸福度。直前の活動がa, b, cどれだったかにより、3つの値が含まれる [a,b,c]
    :param next 次の日に各活動を行って得られる幸福度 [a,b,c]
    :return accの状態でnextの活動を行った場合の新しい累積幸福度 [a,b,c]
    """
    sums = acc[:, None] + next[None, :] # accとnextの要素同士の和を全パターン計算し、3x3の行列にする
    np.fill_diagonal(sums, 0) # 連続で同じ活動ができないという制約は、i != j (対角成分の幸福度を0としてmax計算から除外) で表現する
    return sums.max(axis=0) # nextのindexが同じものの中で最大のものを選ぶ

def solve(activities: np.ndarray) -> int:
    return max(functools.reduce(apply, activities))

print(solve(abc))
