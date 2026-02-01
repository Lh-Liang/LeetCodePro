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
        for (int i = 0; i < n; i++) {
            if (!adj[i].empty()) {
                sort(adj[i].begin(), adj[i].end());
            }
        }

        vector<int> L(n), R(n);
        string dfsStr = "";
        dfsStr.reserve(n);
        int timer = 0;

        // Iterative DFS to build post-order string and record ranges
        vector<int> child_idx(n, 0);
        vector<int> st;
        st.reserve(n);
        st.push_back(0);

        while (!st.empty()) {
            int u = st.back();
            if (child_idx[u] == 0) {
                L[u] = timer;
            }
            if (child_idx[u] < adj[u].size()) {
                int v = adj[u][child_idx[u]];
                child_idx[u]++;
                st.push_back(v);
            } else {
                dfsStr += s[u];
                R[u] = timer;
                timer++;
                st.pop_back();
            }
        }

        // Manacher's Algorithm for palindrome queries in O(1)
        vector<int> d1(n); // Odd palindromes radius (including center)
        for (int i = 0, l = 0, r = -1; i < n; i++) {
            int k = (i > r) ? 1 : min(d1[l + r - i], r - i + 1);
            while (0 <= i - k && i + k < n && dfsStr[i - k] == dfsStr[i + k]) {
                k++;
            }
            d1[i] = k--;
            if (i + k > r) {
                l = i - k;
                r = i + k;
            }
        }

        vector<int> d2(n); // Even palindromes radius (centered between i-1 and i)
        for (int i = 0, l = 0, r = -1; i < n; i++) {
            int k = (i > r) ? 0 : min(d2[l + r - i + 1], r - i + 1);
            while (0 <= i - k - 1 && i + k < n && dfsStr[i - k - 1] == dfsStr[i + k]) {
                k++;
            }
            d2[i] = k--;
            if (i + k > r) {
                l = i - k - 1;
                r = i + k;
            }
        }

        vector<bool> answer(n);
        for (int i = 0; i < n; i++) {
            int len = R[i] - L[i] + 1;
            if (len % 2 == 1) {
                int mid = (L[i] + R[i]) / 2;
                if (d1[mid] >= (len + 1) / 2) {
                    answer[i] = true;
                } else {
                    answer[i] = false;
                }
            } else {
                int mid_high = (L[i] + R[i] + 1) / 2;
                if (d2[mid_high] >= len / 2) {
                    answer[i] = true;
                } else {
                    answer[i] = false;
                }
            }
        }

        return answer;
    }
};
# @lc code=end