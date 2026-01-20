#
# @lc app=leetcode id=3785 lang=cpp
#
# [3785] Minimum Swaps to Avoid Forbidden Values
#

# @lc code=start
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <cmath>

using namespace std;

class Solution {
public:
    int minSwaps(vector<int>& nums, vector<int>& forbidden) {
        int n = nums.size();
        unordered_map<int, int> num_counts;
        unordered_map<int, int> forbidden_counts;
        unordered_map<int, int> bad_counts;
        int total_bad = 0;

        for (int i = 0; i < n; ++i) {
            num_counts[nums[i]]++;
            forbidden_counts[forbidden[i]]++;
            if (nums[i] == forbidden[i]) {
                bad_counts[nums[i]]++;
                total_bad++;
            }
        }

        // Check existence condition: count(nums, x) + count(forbidden, x) <= n
        // We only need to check values that appear in nums or forbidden.
        for (auto const& [val, count] : num_counts) {
            if (count + forbidden_counts[val] > n) {
                return -1;
            }
        }
        // Also check values that might only be in forbidden
        for (auto const& [val, count] : forbidden_counts) {
            if (count + num_counts[val] > n) {
                return -1;
            }
        }

        if (total_bad == 0) return 0;

        int max_bad_group = 0;
        for (auto const& [val, count] : bad_counts) {
            max_bad_group = max(max_bad_group, count);
        }

        // Result is max(ceil(total_bad / 2), max_bad_group)
        return max((total_bad + 1) / 2, max_bad_group);
    }
};
# @lc code=end