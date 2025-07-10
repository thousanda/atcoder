MOD = 10**9 + 7


'''
繰り返し二乗法
 n^p mod m を高速に求める
 O(log p)
 pow(n, p, m) の中身はこんな感じになってる?
'''
def mod_exp(n, p, m):
    if p == 0:
        return 1
    if p == 1:
        return n
    
    if p % 2 == 0:
        return mod_exp(n, p//2, m)** 2 % m
    else:
        return n * mod_exp(n, p-1, m) % m

print('pow:', pow(2, 1000000000, MOD))  # 140625001
print('self inplementation:', mod_exp(2, 1000000000, MOD))  # 140625001
print()


'''
Modular Multiplication Inverse (モジュラ逆数)
 = 合同算術における積の逆元
フェルマーの小定理より
mが素数，nとmが互いに袖あるとき
n^(m-1) ≡ 1 mod 
が成り立つ．これより
n * n(m-2) ≡ 1 mod m
となるため、nの逆元はn^(m-2)
ただし、n^(m-2) mod m は愚直に計算するととても時間がかかるので、繰り返し二乗法で求める
'''
def mod_inv(n, m):
    return pow(n, m-2, m)

print('8^(-1) =', mod_inv(8, MOD), 'mod 10**9 + 7')  # 125000001
print()


'''
nCr mod m
繰り返し二乗法と逆元を使って巨大な数の乗算を回避
'''
def nCr_mod_m(n, r, m):
    if r < 0 or n < r:
        return 0
    # n!
    fact = fact_prev = 1 # 0! = 1! = 1
    for i in range(2, n+1):
        fact = fact_prev * i % m
        fact_prev = fact
    # n!^(-1)
    fact_inv = [0]*(max(r, n-r)+1)
    fact_inv[0] = fact_inv[1] = 1  # 1 = 1 mod m
    for i in range(2, max(r, n-r)+1):
        fact_inv[i] = fact_inv[i-1] * mod_inv(i, m) % m
    return (fact * fact_inv[r] % m) * fact_inv[n-r] % m

print('5C2 =', nCr_mod_m(5, 2, 7), 'mod 7')
print('5C2 =', nCr_mod_m(5, 2, MOD), 'mod 10^9 + 7')
print()


'''
nCr_mod_m
何回も計算する必要がある時は内部に階乗の値を持っておく
n!までを保存しておく実装のため、nには十分に大きい値を設定する
'''
class Factorial_Memory():
    def __init__(self, n, mod):
        self.mod = mod
        
        fact = [0]*(n+1)
        fact_inv = [0]*(n+1)
        # 0! = 1! = 1
        fact[0] = fact[1] = fact_inv[0] = fact_inv[1] = 1 

        ### n! ###
        for i in range(2, n+1):
            fact[i] = fact[i-1] * i % mod

        # n!^(-1)
        for i in range(2, n+1):
            fact_inv[i] = fact_inv[i-1] * self._mod_inv(i, mod) % mod

        self.fact = fact
        self.fact_inv = fact_inv

    def factorial(self, n):
        return self.fact[n]
        
    def nCr(self, n, r):
        if r < 0 or n < r:
            return 0
        fact = self.fact
        fact_inv = self.fact_inv
        m = self.mod
        return (fact[n] * fact_inv[r] % m) * fact_inv[n-r] % m

    def _mod_inv(self, n, mod):
        return pow(n, mod-2, mod)

fact_memory = Factorial_Memory(10, MOD)
print('5! =', fact_memory.factorial(5), 'mod 10**9 + 7')
print('5C2 =', fact_memory.nCr(5, 2), 'mod 10^9 + 7')
print()
