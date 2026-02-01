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
    vector<bool> findAnswer(vector<int>& parent, string s) {
        int n = parent.size();
        vector<vector<int>> adj(n);
        for (int i = 1; i < n; i++) {
            adj[parent[i]].push_back(i);
        }
        // Requirement: children in increasing order
        for (int i = 0; i < n; i++) {
            if (adj[i].size() > 1) sort(adj[i].begin(), adj[i].end());
        }

        vector<int> L(n), R(n);
        string global_str = "";
        global_str.reserve(n);

        // Iterative DFS to handle deep trees and capture substring ranges
        struct Frame {
            int u;
            int child_idx;
        };
        vector<Frame> st;
        st.push_back({0, 0});
        
        while (!st.empty()) {
            Frame& top = st.back();
            int u = top.u;
            if (top.child_idx == 0) {
                L[u] = (int)global_str.size();
            }
            if (top.child_idx < (int)adj[u].size()) {
                int v = adj[u][top.child_idx];
                top.child_idx++;
                st.push_back({v, 0});
            } else {
                global_str += s[u];
                R[u] = (int)global_str.size() - 1;
                st.pop_back();
            }
        }

        // Manacher's Algorithm for O(n) palindrome checks
        string t = "#";
        for (char c : global_str) {
            t += c;
            t += "#";
        }

        int m = (int)t.size();
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
            int len = R[i] - L[i] + 1;
            int center_in_t = L[i] + R[i] + 1;
            answer[i] = (p[center_in_t] >= len);
        }

        return answer;
    }
};
# @lc code=end