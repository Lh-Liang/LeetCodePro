#include <bits/stdc++.h>
using namespace std;

/*
 * @lc app=leetcode id=3470 lang=cpp
 *
 * [3470] Permutations IV
 */

// @lc code=start
class Solution {
public:
    vector<int> permute(int n, long long k) {
        const long long INF = 1000000000000000LL + 1; // 1e15 + 1

        int totalOdd = (n + 1) / 2;
        int totalEven = n / 2;

        // factorials up to 50 (max possible odd/even count when n<=100)
        int maxF = 50;
        vector<long long> fact(maxF + 1, 1);
        for (int i = 1; i <= maxF; i++) {
            __int128 v = (__int128)fact[i - 1] * i;
            fact[i] = (v >= INF) ? INF : (long long)v;
        }

        auto mulCap = [&](long long a, long long b) -> long long {
            __int128 v = (__int128)a * b;
            return (v >= INF) ? INF : (long long)v;
        };

        // startParity: 1 for odd, 0 for even, indicates parity required at next position
        auto ways = [&](int o, int e, int len, int startParity) -> long long {
            if (len == 0) return 1;
            int oddSlots, evenSlots;
            if (startParity == 1) {
                oddSlots = (len + 1) / 2;
                evenSlots = len / 2;
            } else {
                oddSlots = len / 2;
                evenSlots = (len + 1) / 2;
            }
            if (o != oddSlots || e != evenSlots) return 0;
            return mulCap(fact[o], fact[e]);
        };

        vector<char> used(n + 1, 0);
        vector<int> ans;
        ans.reserve(n);

        int o = totalOdd, e = totalEven;
        int prevParity = -1; // unknown for first position

        for (int pos = 0; pos < n; pos++) {
            bool picked = false;
            for (int x = 1; x <= n; x++) {
                if (used[x]) continue;
                int px = (x & 1); // 1 odd, 0 even
                if (prevParity != -1 && px == prevParity) continue;

                int o2 = o - (px == 1);
                int e2 = e - (px == 0);
                int remLen = n - pos - 1;

                long long cnt;
                if (remLen == 0) {
                    cnt = 1;
                } else {
                    int nextParity = 1 - px;
                    cnt = ways(o2, e2, remLen, nextParity);
                }

                if (k > cnt) {
                    k -= cnt;
                } else {
                    used[x] = 1;
                    ans.push_back(x);
                    prevParity = px;
                    o = o2; e = e2;
                    picked = true;
                    break;
                }
            }
            if (!picked) return {};
        }
        return ans;
    }
};
// @lc code=end
