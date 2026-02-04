#
# @lc app=leetcode id=3331 lang=cpp
#
# [3331] Find Subtree Sizes After Changes
#
# @lc code=start
class Solution {
public:
    vector<int> findSubtreeSizes(vector<int>& parent, string s) {
        int n = parent.size();
        vector<vector<int>> children(n);
        for (int i = 1; i < n; ++i) {
            children[parent[i]].push_back(i);
        }
        vector<int> result(n, 0);
        function<void(int)> dfs = [&](int node) {
            result[node] = 1; // count itself
            for (int child : children[node]) {
                dfs(child);
                result[node] += result[child]; // add child subtrees size
            }
        };
        dfs(0); // start DFS from root node 0
        return result; // return calculated subtree sizes
    }
};
# @lc code=end