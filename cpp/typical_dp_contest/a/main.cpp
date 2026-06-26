#include <bits/stdc++.h>
using namespace std;

// TDPC A - コンテスト
// N問の配点 p_i から作れる合計点が何通りあるか (0点を含む) を数える。
// 部分和を bitset で管理し、各問題を「解く/解かない」で左シフトORしていく。
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    // p_i <= 100, N <= 100 なので合計は最大 10000
    bitset<10001> reachable;
    reachable[0] = true;  // 0点 (何も解かない) は常に到達可能

    for (int i = 0; i < n; i++) {
        int p;
        cin >> p;
        reachable |= reachable << p;
    }

    cout << reachable.count() << '\n';
    return 0;
}
