#
# @lc app=leetcode id=3748 lang=cpp
#
# [3748] Count Stable Subarrays
#

# @lc code=start
class Solution {
public:
    vector<long long> countStableSubarrays(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        vector<int> longestStable(n, n); // longest stable segment starting from each index
        
        // Preprocess to find longest stable segments starting at each index
        for (int i = n - 2; i >= 0; --i) {
            if (nums[i] <= nums[i + 1]) {
                longestStable[i] = longestStable[i + 1];
            } else {
                longestStable[i] = i + 1;
            }
        }
        
        vector<long long> ans;
        // Process each query using precomputed stability information
        for (auto &q : queries) {
            int li = q[0], ri = q[1];
            long long count = 0;
            for (int start = li; start <= ri; ++start) {
                int endLimit = min(ri + 1, longestStable[start]);
                count += endLimit - start;
            }
            ans.push_back(count);
        }
        return ans;
    }
};
# @lc code=end