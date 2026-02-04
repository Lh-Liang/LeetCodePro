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
        auto check = [&](int l) {
            int flips = 0;
            int cnt = 1;
            for (int i = 1; i < n; ++i) {
                if (s[i] == s[i-1]) {
                    cnt++;
                    if (cnt > l) {
                        flips++;
                        cnt = 1;
                    }
                } else {
                    cnt = 1;
                }
            }
            return flips <= numOps;
        };
        int ans = n;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (check(mid)) {
                ans = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return ans;
    }
};
# @lc code=end