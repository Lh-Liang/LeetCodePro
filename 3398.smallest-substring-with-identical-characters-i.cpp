#
# @lc app=leetcode id=3398 lang=cpp
#
# [3398] Smallest Substring With Identical Characters I
#

# @lc code=start
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minLength(string s, int numOps) {
        int n = s.length();

        auto check = [&](int k) {
            if (k == 1) {
                int ops0 = 0, ops1 = 0;
                for (int i = 0; i < n; ++i) {
                    // Pattern 0: 010101...
                    if (s[i] != (i % 2 == 0 ? '0' : '1')) ops0++;
                    // Pattern 1: 101010...
                    else ops1++;
                }
                return min(ops0, ops1) <= numOps;
            }

            int totalOps = 0;
            int count = 1;
            for (int i = 1; i < n; ++i) {
                if (s[i] == s[i - 1]) {
                    count++;
                } else {
                    totalOps += count / (k + 1);
                    count = 1;
                }
            }
            totalOps += count / (k + 1);
            return totalOps <= numOps;
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