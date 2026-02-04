#
# @lc app=leetcode id=3525 lang=cpp
#
# [3525] Find X Value of Array II
#
# @lc code=start
class Solution {
public:
    vector<int> resultArray(vector<int>& nums, int k, vector<vector<int>>& queries) {
        vector<int> results;
        for (auto &query : queries) {
            int index = query[0];
            int value = query[1];
            int start = query[2];
            int x = query[3];
            
            // Update nums at index with new value
            nums[index] = value;
            
            // Calculate x-value by iterating over suffixes starting from 'start'
            int count = 0;
            long long product = 1;
            for (int i = start; i < nums.size(); ++i) {
                product = (product * nums[i]) % k;
                if (product == x) {
                    ++count;
                }
            }
            results.push_back(count);
        }
        return results;
    }
};
# @lc code=end