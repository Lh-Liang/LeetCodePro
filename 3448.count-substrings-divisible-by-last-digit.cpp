#
# @lc app=leetcode id=3448 lang=cpp
#
# [3448] Count Substrings Divisible By Last Digit
#

# @lc code=start
class Solution {
public:
    long long countSubstrings(string s) {
        int n = s.size();
        vector<vector<long long>> current(10, vector<long long>(10, 0));
        long long ans = 0;
        for (int j = 0; j < n; ++j) {
            int dig = s[j] - '0';
            vector<vector<long long>> newc(10, vector<long long>(10, 0));
            // Add single digit substring
            for (int dd = 1; dd <= 9; ++dd) {
                int md = dig % dd;
                newc[dd][md]++;
            }
            // Extend previous substrings
            for (int dd = 1; dd <= 9; ++dd) {
                for (int oldm = 0; oldm < dd; ++oldm) {
                    long long num = current[dd][oldm];
                    if (num == 0) continue;
                    int newmd = ((static_cast<long long>(oldm) * 10LL % dd + dig % dd) % dd + dd) % dd;
                    newc[dd][newmd] += num;
                }
            }
            if (dig != 0) {
                ans += newc[dig][0];
            }
            current = std::move(newc);
        }
        return ans;
    }
};
# @lc code=end