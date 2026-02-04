#
# @lc app=leetcode id=3525 lang=cpp
#
# [3525] Find X Value of Array II
#

# @lc code=start
class Solution {
public:
    vector<int> resultArray(vector<int>& nums, int k, vector<vector<int>>& queries) {
        int n = nums.size();
        vector<int> res;
        for (auto& q : queries) {
            int idx = q[0], val = q[1], s = q[2], x = q[3];
            nums[idx] = val;
            int m = n - s;
            int answer = 0;
            // Compute the product of nums[s..j] for all j in [s, n-1]
            int prod = 1;
            for (int j = s; j < n; ++j) {
                prod = (1LL * prod * nums[j]) % k;
                if (prod == x) answer++;
            }
            res.push_back(answer);
        }
        return res;
    }
};
# @lc code=end