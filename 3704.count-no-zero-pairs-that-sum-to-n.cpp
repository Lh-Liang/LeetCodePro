#
# @lc app=leetcode id=3704 lang=cpp
#
# [3704] Count No-Zero Pairs That Sum to N
#
# @lc code=start
#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    long long countNoZeroPairs(long long n) {
        vector<int> dn;
        long long nn = n;
        do {
            dn.push_back(nn % 10);
            nn /= 10;
        } while (nn > 0);
        int L = dn.size();
        long long mem[17][2][2][2][2][2];
        memset(mem, -1, sizeof(mem));
        auto dfs = [&](auto&& self, int pos, int carry, int fa, int ha, int fb, int hb) -> long long {
            if (pos == L) {
                return (carry == 0 && ha == 1 && hb == 1) ? 1LL : 0LL;
            }
            if (mem[pos][carry][fa][ha][fb][hb] != -1) {
                return mem[pos][carry][fa][ha][fb][hb];
            }
            long long res = 0;
            for (int da = 0; da < 10; ++da) {
                if (fa && da != 0) continue;
                int nfa = (da == 0);
                int nha = ha || (da != 0);
                for (int db = 0; db < 10; ++db) {
                    if (fb && db != 0) continue;
                    int nfb = (db == 0);
                    int nhb = hb || (db != 0);
                    int tot = da + db + carry;
                    if (tot % 10 == dn[pos]) {
                        int nc = tot / 10;
                        res += self(self, pos + 1, nc, nfa, nha, nfb, nhb);
                    }
                }
            }
            mem[pos][carry][fa][ha][fb][hb] = res;
            return res;
        };
        return dfs(dfs, 0, 0, 0, 0, 0, 0);
    }
};
# @lc code=end