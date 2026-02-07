#
# @lc app=leetcode id=3748 lang=cpp
#
# [3748] Count Stable Subarrays
#
# @lc code=start
class Solution {
public:
    vector<long long> countStableSubarrays(vector<int>& nums, vector<vector<int>>& queries) {
        vector<long long> results;
        for (const auto& query : queries) {
            int li = query[0], ri = query[1];
            long long count = 0;
            int length = 1; // Track current length of stable sequence
            for (int i = li + 1; i <= ri; ++i) {
                if (nums[i] >= nums[i - 1]) {
                    ++length;
                } else {
                    // Calculate number of stable subarrays from current sequence length
                    count += (long long)(length * (length + 1)) / 2;
                    length = 1; // Reset length for new sequence
                }
            }
            // Handle last segment if it ends with a non-decreasing sequence
            count += (long long)(length * (length + 1)) / 2;
            results.push_back(count);
        }
        return results;
    }
};
# @lc code=end