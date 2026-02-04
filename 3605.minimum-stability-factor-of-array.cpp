#
# @lc app=leetcode id=3605 lang=cpp
#
# [3605] Minimum Stability Factor of Array
#

# @lc code=start
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;

class Solution {
public:
    int minStable(vector<int>& nums, int maxC) {
        int n = nums.size();
        // Helper function: check if all stable subarrays of length > k can be destroyed with <= maxC modifications
        auto canBreak = [&](int k) {
            vector<int> mods;
            int l = 0, r = 0;
            int cur_gcd = 0;
            // Use a sliding window
            while (l < n) {
                r = l;
                cur_gcd = nums[l];
                while (r + 1 < n && r - l + 1 < k + 1) {
                    ++r;
                    cur_gcd = gcd(cur_gcd, nums[r]);
                }
                // Now window is [l, r] with length k+1
                // Check all windows starting from l
                int window_gcd = cur_gcd;
                int end = r;
                while (end < n) {
                    window_gcd = gcd(window_gcd, nums[end]);
                    if (window_gcd >= 2) {
                        mods.push_back(end); // Greedy: pick rightmost to break
                        // Jump over this window
                        l = end + 1;
                        break;
                    }
                    ++end;
                }
                if (end == n) ++l;
            }
            return (int)mods.size() <= maxC;
        };
        // Binary search for minimal k
        int left = 0, right = n, res = n;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (canBreak(mid)) {
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