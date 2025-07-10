'''
https://qiita.com/snow67675476/items/e87ddb9285e27ea555f8

nを素因数分解
2以上の整数n => [[素因数, 指数], ...]の2次元リスト
・試し割り法
・2からn^(1/2)までチェック
・O(n^(1/2))

1を引数として実行すると、[1, 1]　が返ってくる
'''

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

pf = factorization(24)
print(pf)

pf = factorization(1)
print(pf)
