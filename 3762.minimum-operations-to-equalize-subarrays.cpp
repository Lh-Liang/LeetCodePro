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
        for (auto &q : queries) {
            int li = q[0], ri = q[1];
            int base = nums[li];
            bool feasible = true;
            long long ops = 0;
            for (int i = li; i <= ri; ++i) {
                if ((nums[i] - base) % k != 0) {
                    feasible = false;
                    break;
                } else {
                    ops += abs(nums[i] - base) / k;
                }
            }
            ans.push_back(feasible ? ops : -1);
        }
        return ans;
    }
};
# @lc code=end