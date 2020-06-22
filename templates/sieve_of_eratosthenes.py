def sieve(N):
    # 昇順リストの用意
    A_list = [i for i in range(2, N+1)]
    print(f'{A_list=}')
    limit = A_list[-1]

    # ふるいにかけられたかどうかを示すbooleanの辞書
    sieve = {i: True for i in A_list}
    print(sieve)

    # 順にふるいにかける
    for a in A_list:
        print(f'{a=}')
        if not sieve[a]:
            print('continue')
            continue
        for i in range(2*a, limit+1, a):  # 2a, 3a, 4a, ..., と調べる
            if i in sieve:
                sieve[i] = False
        print(f'{sieve=}')

    # 結果をまとめる
    primes = []
    for a in A_list:
        if sieve[a]:
            primes.append(a)
    return primes

print(sieve(12))
