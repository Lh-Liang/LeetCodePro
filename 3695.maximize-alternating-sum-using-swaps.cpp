# @lc app=leetcode id=3695 lang=cpp
# [3695] Maximize Alternating Sum Using Swaps
# 
# @lc code=start
class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums, vector<vector<int>>& swaps) {
        int n = nums.size();
        vector<int> parent(n);
        iota(parent.begin(), parent.end(), 0); // Initialize union-find structure
        function<int(int)> find = [&](int x) { return x == parent[x] ? x : parent[x] = find(parent[x]); }; // Find with path compression
        auto unite = [&](int x, int y) { parent[find(x)] = find(y); }; // Union operation
        // Unite indices based on swaps
        for (const auto& s : swaps)
            unite(s[0], s[1]); 
        unordered_map<int, vector<int>> groups; 
        for (int i = 0; i < n; ++i) 
            groups[find(i)].push_back(i); 
        vector<int> sorted_nums(n); 
        for (auto& [root, group] : groups) {
            vector<int> values;
            for (int idx : group)
                values.push_back(nums[idx]);
            sort(values.begin(), values.end(), greater<>()); // Sort in descending order to maximize sum at even positions
            sort(group.begin(), group.end());
            for (int i = 0; i < group.size(); ++i)
                sorted_nums[group[i]] = values[i];
        }
        long long max_sum = 0;
        for (int i = 0; i < n; ++i) {
            if (i % 2 == 0) max_sum += sorted_nums[i]; else max_sum -= sorted_nums[i];
        }
        return max_sum;
    }
};
# @lc code=end