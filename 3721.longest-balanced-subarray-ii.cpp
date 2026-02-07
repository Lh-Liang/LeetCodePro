# @lc app=leetcode id=3721 lang=cpp
# [3721] Longest Balanced Subarray II

# @lc code=start
class Solution {
public:
    int longestBalanced(vector<int>& nums) {
        unordered_map<int, int> evenCounts;
        unordered_map<int, int> oddCounts;
        int left = 0;
        int maxLength = 0;
        for (int right = 0; right < nums.size(); ++right) {
            if (nums[right] % 2 == 0) {
                evenCounts[nums[right]]++;
            } else {
                oddCounts[nums[right]]++;
            }
            while (evenCounts.size() != oddCounts.size()) {
                if (nums[left] % 2 == 0) {
                    if (--evenCounts[nums[left]] == 0) {
                        evenCounts.erase(nums[left]);
                    }
                } else {
                    if (--oddCounts[nums[left]] == 0) {
                        oddCounts.erase(nums[left]);
                    }
                }
                ++left;
            }
            maxLength = max(maxLength, right - left + 1);
        }
        return maxLength;
    }
};
# @lc code=end