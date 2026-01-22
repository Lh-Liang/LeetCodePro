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
        unordered_map<int, vector<int>> mp;
        for (int i = 0; i < n; ++i) {
            mp[nums[i]].push_back(i);
        }
        vector<int> res(n, -1);
        for (auto& p : mp) {
            const vector<int>& indices = p.second;
            int m = indices.size();
            if (m == 1) continue;
            for (int j = 0; j < m; ++j) {
                int idx = indices[j];
                int left_idx = indices[(j - 1 + m) % m];
                int right_idx = indices[(j + 1) % m];
                int dist_left = abs(idx - left_idx);
                dist_left = min(dist_left, n - dist_left);
                int dist_right = abs(idx - right_idx);
                dist_right = min(dist_right, n - dist_right);
                res[idx] = min(dist_left, dist_right);
            }
        }
        vector<int> ans;
        ans.reserve(queries.size());
        for (int q : queries) {
            ans.push_back(res[q]);
        }
        return ans;
    }
};
# @lc code=end