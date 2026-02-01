#
# @lc app=leetcode id=3327 lang=cpp
#
# [3327] Check if DFS Strings Are Palindromes
#

# @lc code=start
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    void dfs(int u, const vector<vector<int>>& adj, const string& s, string& globalStr, int& time, vector<int>& start, vector<int>& end) {
        int curr_start = time;
        for (int v : adj[u]) {
            dfs(v, adj, s, globalStr, time, start, end);
        }
        start[u] = curr_start;
        globalStr[time] = s[u];
        end[u] = time;
        time++;
    }

    vector<bool> findAnswer(vector<int>& parent, string s) {
        int n = parent.size();
        vector<vector<int>> adj(n);
        for (int i = 1; i < n; i++) {
            adj[parent[i]].push_back(i);
        }
        for (int i = 0; i < n; i++) {
            sort(adj[i].begin(), adj[i].end());
        }

        string globalStr(n, ' ');
        vector<int> start(n), end(n);
        int time = 0;
        dfs(0, adj, s, globalStr, time, start, end);

        // Manacher's algorithm to precompute palindrome radii
        string t(2 * n + 1, '#');
        for (int i = 0; i < n; i++) {
            t[2 * i + 1] = globalStr[i];
        }

        int m = t.size();
        vector<int> p(m, 0);
        int center = 0, right = 0;
        for (int i = 0; i < m; i++) {
            int mirr = 2 * center - i;
            if (i < right) p[i] = min(right - i, p[mirr]);
            while (i + 1 + p[i] < m && i - 1 - p[i] >= 0 && t[i + 1 + p[i]] == t[i - 1 - p[i]]) {
                p[i]++;
            }
            if (i + p[i] > right) {
                center = i;
                right = i + p[i];
            }
        }

        vector<bool> answer(n);
        for (int i = 0; i < n; i++) {
            int L = start[i];
            int R = end[i];
            int len = R - L + 1;
            // Map substring center in globalStr to center index in character-padded string t
            int t_center = L + R + 1;
            // If the palindrome radius at this center covers the substring length, it's a palindrome
            answer[i] = (p[t_center] >= len);
        }
        return answer;
    }
};
# @lc code=end