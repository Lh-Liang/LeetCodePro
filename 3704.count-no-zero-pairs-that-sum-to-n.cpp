#
# @lc app=leetcode id=3704 lang=cpp
#
# [3704] Count No-Zero Pairs That Sum to N
#
# @lc code=start
class Solution {
public:
    long long countNoZeroPairs(long long n) {
        std::string s = std::to_string(n);
        int sz = s.size();
        // dp[pos][carry][tight] = number of ways
        std::unordered_map<long long, long long> memo;

        // pos: digit position (from right), carry: carry from lower digits, tight: are we tight to n so far
        std::function<long long(int,int,bool)> dfs = [&](int pos, int carry, bool tight) -> long long {
            if (pos == -1) return carry == 0 ? 1 : 0;
            long long key = ((long long)pos<<32) | ((long long)carry<<1) | tight;
            if (!tight && memo.count(key)) return memo[key];
            long long res = 0;
            int nd = s[sz-1-pos] - '0';
            for (int da = 1; da <= 9; ++da) {
                for (int db = 1; db <= 9; ++db) {
                    int sum = da + db + carry;
                    int cd = sum % 10;
                    int ncarry = sum / 10;
                    if (tight && cd > nd) continue;
                    if ((tight && cd == nd) || !tight) {
                        bool ntight = tight && (cd == nd);
                        res += dfs(pos-1, ncarry, ntight);
                    }
                }
            }
            if (!tight) memo[key] = res;
            return res;
        };
        return dfs(sz-1,0,true);
    }
};
# @lc code=end