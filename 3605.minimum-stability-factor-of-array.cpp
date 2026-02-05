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
        // Helper: Check if all stable subarrays of length k can be broken with at most maxC changes
        auto can_break = [&](int k) {
            // prefix/suffix GCDs for O(1) range-gcd queries
            vector<int> prefix(n+1, 0), suffix(n+1, 0);
            for (int i = 0; i < n; ++i)
                prefix[i+1] = gcd(prefix[i], nums[i]);
            for (int i = n-1; i >= 0; --i)
                suffix[i] = gcd(suffix[i+1], nums[i]);
            for (int i = 0; i + k <= n; ++i) {
                int window_gcd = prefix[i+k] == prefix[i] ? nums[i] : gcd(prefix[i], suffix[i+k]);
                // Actually, recompute GCD of window directly
                int g = nums[i];
                for (int j = i+1; j < i+k; ++j) g = gcd(g, nums[j]);
                if (g >= 2) {
                    // Can we break this window with <= maxC changes?
                    // Try all possible positions to change.
                    int cnt = 0;
                    for (int j = i; j < i+k; ++j) if (nums[j] % g == 0) ++cnt;
                    if (cnt > maxC) return false;
                }
            }
            return true;
        };
        int lo = 1, hi = n, ans = n;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (can_break(mid)) {
                ans = mid;
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        return ans == n && !can_break(n) ? 0 : ans;
    }
};
# @lc code=end