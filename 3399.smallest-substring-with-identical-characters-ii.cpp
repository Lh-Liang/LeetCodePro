#
# @lc app=leetcode id=3399 lang=cpp
#
# [3399] Smallest Substring With Identical Characters II
#

# @lc code=start
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    int minLength(string s, int numOps) {
        int n = s.length();
        
        auto check = [&](int k) -> bool {
            if (k == 1) {
                int flips_pattern1 = 0;
                int flips_pattern2 = 0;
                for (int i = 0; i < n; ++i) {
                    // Pattern 1: 010101...
                    if (s[i] != (i % 2 == 0 ? '0' : '1')) flips_pattern1++;
                    // Pattern 2: 101010...
                    if (s[i] != (i % 2 == 0 ? '1' : '0')) flips_pattern2++;
                }
                return min(flips_pattern1, flips_pattern2) <= numOps;
            } else {
                int total_flips = 0;
                int current_run_len = 0;
                for (int i = 0; i < n; ++i) {
                    current_run_len++;
                    if (i == n - 1 || s[i] != s[i + 1]) {
                        total_flips += current_run_len / (k + 1);
                        current_run_len = 0;
                    }
                }
                return total_flips <= numOps;
            }
        };
        
        int low = 1, high = n, ans = n;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (check(mid)) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        
        return ans;
    }
};
# @lc code=end