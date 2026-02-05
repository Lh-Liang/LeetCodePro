#
# @lc app=leetcode id=3327 lang=cpp
#
# [3327] Check if DFS Strings Are Palindromes
#

# @lc code=start
class Solution {
public:
    vector<bool> findAnswer(vector<int>& parent, string s) {
        int n = parent.size();
        vector<vector<int>> tree(n);
        for (int i = 1; i < n; ++i) {
            tree[parent[i]].push_back(i);
        }
        for (int i = 0; i < n; ++i) {
            sort(tree[i].begin(), tree[i].end());
        }
        vector<bool> answer(n);
        string dfsStr;
        function<void(int)> dfs = [&](int x) {
            for (int y : tree[x]) dfs(y);
            dfsStr += s[x];
        };
        for (int i = 0; i < n; ++i) {
            dfsStr.clear();
            dfs(i);
            string t = dfsStr;
            reverse(t.begin(), t.end());
            answer[i] = (dfsStr == t);
        }
        return answer;
    }
};
# @lc code=end