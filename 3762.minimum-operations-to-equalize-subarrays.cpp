#
# @lc app=leetcode id=3762 lang=cpp
#
# [3762] Minimum Operations to Equalize Subarrays
#

# @lc code=start
class Solution {
public:
    vector<long long> minOperations(vector<int>& nums, int k, vector<vector<int>>& queries) {
        vector<long long> ans;
        for (auto& query : queries) {
            int l = query[0], r = query[1];
            vector<int> subarray(nums.begin() + l, nums.begin() + r + 1);
            sort(subarray.begin(), subarray.end());
            int median = subarray[subarray.size() / 2];
            long long operations = 0;
            bool possible = true;
            for (int num : subarray) {
                int diff = abs(num - median);
                if (diff % k != 0) {
                    possible = false;
                    break;
                } else {
                    operations += diff / k;
                }
            }
            ans.push_back(possible ? operations : -1);
        }
        return ans;
    }
}; 
# @lc code=end