#
# @lc app=leetcode id=3488 lang=cpp
#
# [3488] Closest Equal Element Queries
#

# @lc code=start
class Solution {
public:
    vector<int> solveQueries(vector<int>& nums, vector<int>& queries) {
        int n = nums.size();
        unordered_map<int, vector<int>> pos;
        for (int i = 0; i < n; ++i) {
            pos[nums[i]].push_back(i);
        }
        vector<int> ans;
        for (int q : queries) {
            int val = nums[q];
            vector<int>& indices = pos[val];
            int m = indices.size();
            if (m == 1) {
                ans.push_back(-1);
                continue;
            }
            auto it = lower_bound(indices.begin(), indices.end(), q);
            int k = it - indices.begin();
            int left_k = (k - 1 + m) % m;
            int right_k = (k + 1) % m;
            int left_pos = indices[left_k];
            int right_pos = indices[right_k];
            int d1 = abs(q - left_pos);
            d1 = min(d1, n - d1);
            int d2 = abs(q - right_pos);
            d2 = min(d2, n - d2);
            ans.push_back(min(d1, d2));
        }
        return ans;
    }
};
# @lc code=end