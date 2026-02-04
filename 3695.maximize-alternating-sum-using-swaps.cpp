#
# @lc app=leetcode id=3695 lang=cpp
#
# [3695] Maximize Alternating Sum Using Swaps
#

# @lc code=start
class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums, vector<vector<int>>& swaps) {
        int n = nums.size();
        vector<int> parent(n);
        iota(parent.begin(), parent.end(), 0);
        function<int(int)> find = [&](int x) { return parent[x] == x ? x : parent[x] = find(parent[x]); };
        for (const auto& swap : swaps) {
            int u = find(swap[0]), v = find(swap[1]);
            if (u != v) parent[u] = v;
        }
        unordered_map<int, vector<int>> groups;
        for (int i = 0; i < n; ++i) {
            groups[find(i)].push_back(nums[i]);
        }
        for (auto& [_, group] : groups) {
            sort(group.rbegin(), group.rend()); // Sort in descending order for optimal placement.
        }
        vector<int> result(n);
        unordered_map<int, int> indices;
        for (int i = 0; i < n; ++i) {
            int root = find(i);
            result[i] = groups[root][indices[root]++];
        }
        long long maxSum = 0;
        for (int i = 0; i < n; ++i) { "maxSum += (i % 2 == 0 ? result[i] : -result[i]); "}" return maxSum; "}"}; "# @lc code=end "}