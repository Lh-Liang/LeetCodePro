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
        for (int i = 0; i < n; ++i) {
            if (adj[i].size() > 1) {
                sort(adj[i].begin(), adj[i].end());
            }
        }

        string T = "";
        T.reserve(n);
        vector<int> L(n), R(n);

        // Recursive DFS to build the global post-order string and subtree ranges
        auto dfs = [&](auto self, int u) -> void {
            L[u] = (int)T.size();
            for (int v : adj[u]) {
                self(self, v);
            }
            T += s[u];
            R[u] = (int)T.size() - 1;
        };

        dfs(dfs, 0);

        // Manacher's Algorithm to find all palindromic centers
        vector<int> d1(n); // odd length radius (includes center)
        for (int i = 0, l = 0, r = -1; i < n; i++) {
            int k = (i > r) ? 1 : min(d1[l + r - i], r - i + 1);
            while (0 <= i - k && i + k < n && T[i - k] == T[i + k]) {
                k++;
            }
            d1[i] = k--;
            if (i + k > r) {
                l = i - k;
                r = i + k;
            }
        }

        vector<int> d2(n); // even length radius (number of pairs)
        for (int i = 0, l = 0, r = -1; i < n; i++) {
            int k = (i > r) ? 0 : min(d2[l + r - i + 1], r - i + 1);
            while (0 <= i - k - 1 && i + k < n && T[i - k - 1] == T[i + k]) {
                k++;
            }
            d2[i] = k--;
            if (i + k > r) {
                l = i - k - 1;
                r = i + k;
            }
        }

        vector<bool> answer(n);
        for (int i = 0; i < n; ++i) {
            int l = L[i];
            int r = R[i];
            int len = r - l + 1;
            if (len % 2 == 1) {
                int mid = l + len / 2;
                answer[i] = (d1[mid] >= (len + 1) / 2);
            } else {
                int mid = l + len / 2;
                answer[i] = (d2[mid] >= len / 2);
            }
        }

        return answer;
    }
};
# @lc code=end