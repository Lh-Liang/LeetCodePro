#
# @lc app=leetcode id=3399 lang=cpp
#
# [3399] Smallest Substring With Identical Characters II
#

# @lc code=start
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minLength(string s, int numOps) {
        int n = s.length();

        auto check = [&](int k) -> bool {
            if (k == 1) {
                int ops0 = 0;
                for (int i = 0; i < n; ++i) {
                    char target = (i % 2 == 0) ? '0' : '1';
                    if (s[i] != target) ops0++;
                }
                return min(ops0, n - ops0) <= numOps;
            } else {
                int totalOps = 0;
                int count = 0;
                for (int i = 0; i < n; ++i) {
                    if (i > 0 && s[i] == s[i - 1]) {
                        count++;
                    } else {
                        totalOps += count / (k + 1);
                        count = 1;
                    }
                }
                totalOps += count / (k + 1);
                return totalOps <= numOps;
            }
        };

        int left = 1, right = n, ans = n;
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