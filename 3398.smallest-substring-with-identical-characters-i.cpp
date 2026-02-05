#
# @lc app=leetcode id=3398 lang=cpp
#
# [3398] Smallest Substring With Identical Characters I
#

# @lc code=start
class Solution {
public:
    int minLength(string s, int numOps) {
        int n = s.size();
        int left = 1, right = n;
        auto canAchieve = [&](int maxLen) {
            int flips = 0, cnt = 1;
            for (int i = 1; i < n; ++i) {
                if (s[i] == s[i-1]) {
                    ++cnt;
                } else {
                    if (cnt > maxLen) flips += (cnt - 1) / maxLen;
                    cnt = 1;
                }
            }
            if (cnt > maxLen) flips += (cnt - 1) / maxLen;
            return flips <= numOps;
        };
        int res = n;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (canAchieve(mid)) {
                res = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return res;
    }
};
# @lc code=end