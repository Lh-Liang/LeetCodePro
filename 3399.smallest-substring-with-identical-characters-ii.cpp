#
# @lc app=leetcode id=3399 lang=cpp
#
# [3399] Smallest Substring With Identical Characters II
#

# @lc code=start
class Solution {
public:
    int minLength(string s, int numOps) {
        int n = s.size();
        int left = 1, right = n;
        auto can = [&](int k, char ch) {
            int flips = 0, res = n+1;
            for (int i = 0, j = 0; i < n; ++i) {
                if (s[i] != ch) ++flips;
                if (i - j + 1 > k) {
                    if (s[j++] != ch) --flips;
                }
                if (i - j + 1 == k && flips <= numOps) return true;
            }
            return false;
        };
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (can(mid, '0') || can(mid, '1')) right = mid;
            else left = mid + 1;
        }
        return left;
    }
};
# @lc code=end