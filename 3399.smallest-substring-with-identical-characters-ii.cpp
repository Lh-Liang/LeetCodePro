#
# @lc app=leetcode id=3399 lang=cpp
#
# [3399] Smallest Substring With Identical Characters II
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
        
        // Pre-calculate block lengths for k > 1
        vector<int> blocks;
        if (n > 0) {
            int count = 1;
            for (int i = 1; i < n; ++i) {
                if (s[i] == s[i - 1]) {
                    count++;
                } else {
                    blocks.push_back(count);
                    count = 1;
                }
            }
            blocks.push_back(count);
        }

        auto check = [&](int k) {
            if (k == 1) {
                int f1 = 0, f2 = 0;
                for (int i = 0; i < n; ++i) {
                    if (s[i] != (i % 2 == 0 ? '0' : '1')) f1++;
                    else f2++;
                }
                return min(f1, f2) <= numOps;
            } else {
                int total = 0;
                for (int L : blocks) {
                    total += L / (k + 1);
                }
                return total <= numOps;
            }
        };

        int low = 1, high = n;
        int ans = n;
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