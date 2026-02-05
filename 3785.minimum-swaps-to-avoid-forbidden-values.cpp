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
        vector<int> conflicted;
        for (int i = 0; i < n; ++i) {
            if (nums[i] == forbidden[i]) {
                conflicted.push_back(i);
            }
        }
        if (conflicted.empty()) return 0;
        unordered_map<int, vector<int>> value_indices;
        for (int i = 0; i < n; ++i) {
            value_indices[nums[i]].push_back(i);
        }
        vector<bool> used(n, false);
        int swaps = 0;
        for (int idx : conflicted) {
            if (used[idx]) continue;
            bool found = false;
            for (int j = 0; j < n; ++j) {
                if (j == idx || used[j]) continue;
                if (nums[j] != forbidden[idx] && nums[idx] != forbidden[j]) {
                    used[idx] = used[j] = true;
                    ++swaps;
                    found = true;
                    break;
                }
            }
            if (!found) {
                return -1;
            }
        }
        return swaps;
    }
};
# @lc code=end