#
# @lc app=leetcode id=3704 lang=cpp
#
# [3704] Count No-Zero Pairs That Sum to N
#
# @lc code=start
class Solution {
public:
    long long countNoZeroPairs(long long n) {
        // Convert n to digits (least significant first)
        std::vector<int> digits;
        long long tmp = n;
        while (tmp > 0) {
            digits.push_back(tmp % 10);
            tmp /= 10;
        }
        int len = digits.size();
        // Memoization: dp[pos][carry]
        std::map<std::pair<int, int>, long long> memo;
        std::function<long long(int, int)> dfs = [&](int pos, int carry) -> long long {
            if (pos == len) {
                return carry == 0 ? 1 : 0;
            }
            auto key = std::make_pair(pos, carry);
            if (memo.count(key)) return memo[key];
            long long res = 0;
            int target = digits[pos];
            // Try all possible (da, db) in 1..9 (no zero digits)
            for (int da = 1; da <= 9; ++da) {
                for (int db = 1; db <= 9; ++db) {
                    int sum = da + db + carry;
                    if (sum % 10 == target) {
                        int next_carry = sum / 10;
                        res += dfs(pos + 1, next_carry);
                    }
                }
            }
            return memo[key] = res;
        };
        return dfs(0, 0);
    }
};
# @lc code=end