#
# @lc app=leetcode id=3785 lang=cpp
#
# [3785] Minimum Swaps to Avoid Forbidden Values
#

# @lc code=start
class Solution {
public:
    int minSwaps(vector<int>& nums, vector<int>& forbidden) {
        int n = nums.size();
        int swaps = 0;
        vector<bool> visited(n, false); // Track visited indices
        for (int i = 0; i < n; ++i) {
            if (nums[i] != forbidden[i] || visited[i]) continue;
            bool swapped = false;
            // Find a suitable swap candidate.
            for (int j = 0; j < n && !swapped; ++j) {
                if (i != j && nums[j] != forbidden[j] && nums[i] != forbidden[j] && nums[j] != forbidden[i]) {
                    swap(nums[i], nums[j]);
                    ++swaps;
                    swapped = true;
                    visited[i] = visited[j] = true; // Mark as visited
                }
            }
            // If no suitable candidate found, return -1.
            if (!swapped) return -1;
        }
        // Verification step: Ensure no element equals its forbidden counterpart.
        for (int k = 0; k < n; ++k) {
            if (nums[k] == forbidden[k]) return -1;
        }
        return swaps;
    }
}; 
# @lc code=end