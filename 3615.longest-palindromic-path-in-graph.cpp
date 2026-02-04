#
# @lc app=leetcode id=3615 lang=cpp
#
# [3615] Longest Palindromic Path in Graph
#

# @lc code=start
class Solution {
public:
    int maxLen(int n, vector<vector<int>>& edges, string label) {
        auto isPalindrome = [](const string& s) {
            int l = 0, r = s.size() - 1;
            while (l < r) {
                if (s[l++] != s[r--]) return false;
            }
            return true;
        };
        vector<vector<int>> g(n);
        for (const auto& e : edges) {
            g[e[0]].push_back(e[1]);
            g[e[1]].push_back(e[0]);
        }
        int res = 1;
        vector<bool> visited(n);
        string path;
        function<void(int)> dfs = [&](int u) {
            visited[u] = true;
            path.push_back(label[u]);
            if (isPalindrome(path)) {
                res = max(res, (int)path.size());
            }
            for (int v : g[u]) {
                if (!visited[v]) {
                    dfs(v);
                }
            }
            path.pop_back();
            visited[u] = false;
        };
        for (int i = 0; i < n; ++i) {
            fill(visited.begin(), visited.end(), false);
            path.clear();
            dfs(i);
        }
        return res;
    }
};
# @lc code=end