#
# @lc app=leetcode id=3748 lang=cpp
#
# [3748] Count Stable Subarrays
#

# @lc code=start
class Solution {
public:
    vector<long long> countStableSubarrays(vector<int>& nums, vector<vector<int>>& queries) {
        vector<long long> ans(queries.size(), 0);
        for (int q = 0; q < queries.size(); ++q) {
            int l = queries[q][0], r = queries[q][1];
            long long count = 0;
            int start = l;
            for (int end = l; end <= r; ++end) {
                while (start < end && nums[start] > nums[end]) {
                    ++start;
                }
                count += end - start + 1;
            }
            ans[q] = count;
        }
        return ans;
    }
};
# @lc code=end