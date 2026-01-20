#
# @lc app=leetcode id=3327 lang=cpp
#
# [3327] Check if DFS Strings Are Palindromes
#

# @lc code=start
#include <vector>
#include <string>
#include <algorithm>
#include <stack>

using namespace std;

class Solution {
public:
    vector<bool> findAnswer(vector<int>& parent, string s) {
        int n = parent.size();
        vector<vector<int>> adj(n);
        for (int i = 1; i < n; i++) {
            adj[parent[i]].push_back(i);
        }

        string totalDfsStr = "";
        totalDfsStr.reserve(n);
        vector<int> start(n), end(n);
        stack<pair<int, int>> st;
        st.push({0, 0});
        
        // Iterative post-order traversal to build the DFS string and record ranges
        while (!st.empty()) {
            int u = st.top().first;
            int& childIdx = st.top().second;
            if (childIdx == 0) {
                start[u] = totalDfsStr.size();
            }
            if (childIdx < adj[u].size()) {
                int v = adj[u][childIdx];
                childIdx++;
                st.push({v, 0});
            } else {
                totalDfsStr += s[u];
                end[u] = (int)totalDfsStr.size() - 1;
                st.pop();
            }
        }

        // Manacher's Algorithm to find all palindromic centers
        string t = "#";
        for (char c : totalDfsStr) {
            t += c;
            t += "#";
        }

        int m = t.size();
        vector<int> d(m, 0);
        int l = 0, r = -1;
        for (int i = 0; i < m; i++) {
            int k = (i > r) ? 1 : min(d[l + r - i], r - i + 1);
            while (i - k >= 0 && i + k < m && t[i - k] == t[i + k]) {
                k++;
            }
            d[i] = k--;
            if (i + k > r) {
                l = i - k;
                r = i + k;
            }
        }

        vector<bool> ans(n);
        for (int i = 0; i < n; i++) {
            int L = start[i];
            int R = end[i];
            int len = R - L + 1;
            // Mapping substring [L, R] to center in t
            int C = L + R + 1;
            // d[C]-1 is the length of the longest palindrome centered at C in totalDfsStr
            if (d[C] - 1 >= len) {
                ans[i] = true;
            } else {
                ans[i] = false;
            }
        }

        return ans;
    }
};
# @lc code=end