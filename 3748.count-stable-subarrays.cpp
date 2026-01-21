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
        vector<int> max_len(n, 1);
        
        // Precompute the maximum length of non-decreasing sequence starting at each position
        for (int i = n - 2; i >= 0; i--) {
            if (nums[i] <= nums[i + 1]) {
                max_len[i] = max_len[i + 1] + 1;
            }
        }
        
        vector<long long> result;
        for (const auto& query : queries) {
            int li = query[0];
            int ri = query[1];
            long long count = 0;
            
            for (int i = li; i <= ri; i++) {
                count += min(max_len[i], ri - i + 1);
            }
            
            result.push_back(count);
        }
        
        return result;
    }
};
# @lc code=end