#
# @lc app=leetcode id=3448 lang=cpp
#
# [3448] Count Substrings Divisible By Last Digit
#

# @lc code=start
#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    long long countSubstrings(string s) {
        int n = s.size();
        long long res = 0;
        for (int d = 1; d <= 9; ++d) {
            unordered_map<int, int> cnt;
            cnt[0] = 1; // empty prefix
            int mod = 0;
            int pow10 = 1;
            for (int i = 0; i < n; ++i) {
                int x = s[i] - '0';
                mod = (mod * 10 + x) % d;
                if (x == d) {
                    res += cnt[mod];
                }
                if (i+1 < n && s[i+1] - '0' == d) {
                    cnt[mod]++;
                }
            }
        }
        return res;
    }
};
# @lc code=end