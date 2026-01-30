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
        for (int i = 1; i < n; ++i) {
            adj[parent[i]].push_back(i);
        }
        // Ensure children are visited in increasing order
        for (int i = 0; i < n; ++i) {
            sort(adj[i].begin(), adj[i].end());
        }

        string T = "";
        T.reserve(n);
        vector<int> start(n), end(n);
        
        // Iterative post-order DFS to build the global string and record ranges
        struct Frame {
            int u;
            int child_idx;
        };
        vector<Frame> st;
        st.reserve(n);
        st.push_back({0, 0});
        
        while (!st.empty()) {
            int u = st.back().u;
            int c_idx = st.back().child_idx;
            
            if (c_idx == 0) {
                start[u] = (int)T.size();
            }
            
            if (c_idx < (int)adj[u].size()) {
                st.back().child_idx++;
                st.push_back({adj[u][c_idx], 0});
            } else {
                T += s[u];
                end[u] = (int)T.size() - 1;
                st.pop_back();
            }
        }

        // Manacher's Algorithm to find all palindromic substrings in O(n)
        string p = "#";
        p.reserve(2 * n + 1);
        for (char c : T) {
            p += c;
            p += "#";
        }
        
        int m = p.size();
        vector<int> d(m, 0);
        int center = 0, right = 0;
        for (int i = 0; i < m; i++) {
            int mirror = 2 * center - i;
            if (i < right)
                d[i] = min(right - i, d[mirror]);
            
            while (i + 1 + d[i] < m && i - 1 - d[i] >= 0 && p[i + 1 + d[i]] == p[i - 1 - d[i]])
                d[i]++;
            
            if (i + d[i] > right) {
                center = i;
                right = i + d[i];
            }
        }

        // Map node ranges to Manacher radii
        vector<bool> answer(n);
        for (int i = 0; i < n; i++) {
            int L = start[i];
            int R = end[i];
            int len = R - L + 1;
            // The center of range [L, R] in the '#' padded string is always L + R + 1
            int C = L + R + 1;
            // d[C] is the radius of the palindrome in the original string T
            answer[i] = (d[C] >= len);
        }

        return answer;
    }
};
# @lc code=end