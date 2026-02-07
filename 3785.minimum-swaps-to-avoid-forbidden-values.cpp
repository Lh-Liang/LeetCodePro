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
        for (int i = 0; i < n; ++i) {
            if (nums[i] == forbidden[i]) {
                bool swapped = false;
                for (int j = i + 1; j < n; ++j) {
                    if (nums[j] != forbidden[i] && nums[j] != forbidden[j]) {
                        std::swap(nums[i], nums[j]);
                        ++swaps;
                        swapped = true;
                        break;
                    }
                }
                if (!swapped) return -1; // Return -1 if no valid swap is found
            }
        }
        return swaps; // Return total number of swaps performed
    }
};
# @lc code=end