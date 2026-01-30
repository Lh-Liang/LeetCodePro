#
# @lc app=leetcode id=3455 lang=cpp
#
# [3455] Shortest Matching Substring
#

# @lc code=start
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> find_all(const string& s, const string& p) {
        if (p.empty()) return {};
        int n = s.length(), m = p.length();
        if (m > n) return {};
        vector<int> pi(m);
        for (int i = 1, j = 0; i < m; i++) {
            while (j > 0 && p[i] != p[j]) j = pi[j - 1];
            if (p[i] == p[j]) j++;
            pi[i] = j;
        }
        vector<int> res;
        for (int i = 0, j = 0; i < n; i++) {
            while (j > 0 && s[i] != p[j]) j = pi[j - 1];
            if (s[i] == p[j]) j++;
            if (j == m) {
                res.push_back(i - m + 1);
                j = pi[j - 1];
            }
        }
        return res;
    }

    int shortestMatchingSubstring(string s, string p) {
        int n = s.length();
        int idx1 = p.find('*');
        int idx2 = p.find('*', idx1 + 1);
        string p0 = p.substr(0, idx1);
        string p1 = p.substr(idx1 + 1, idx2 - idx1 - 1);
        string p2 = p.substr(idx2 + 1);
        int L0 = p0.length(), L1 = p1.length(), L2 = p2.length();

        vector<int> pos0 = find_all(s, p0);
        vector<int> pos1 = find_all(s, p1);
        vector<int> pos2 = find_all(s, p2);

        if (!p0.empty() && pos0.empty()) return -1;
        if (!p1.empty() && pos1.empty()) return -1;
        if (!p2.empty() && pos2.empty()) return -1;

        vector<int> best_i(n + 1, -1);
        if (p0.empty()) {
            for (int j = 0; j <= n; j++) best_i[j] = j;
        } else {
            int cur = -1;
            int ptr = 0;
            for (int j = 0; j <= n; j++) {
                while (ptr < pos0.size() && pos0[ptr] + L0 <= j) {
                    cur = pos0[ptr];
                    ptr++;
                }
                best_i[j] = cur;
            }
        }

        vector<int> best_k(n + 1, -1);
        if (p2.empty()) {
            for (int j = 0; j <= n; j++) {
                if (j + L1 <= n) best_k[j] = j + L1;
            }
        } else {
            int cur = -1;
            int ptr = pos2.size() - 1;
            for (int j = n; j >= 0; j--) {
                while (ptr >= 0 && pos2[ptr] >= j + L1) {
                    cur = pos2[ptr];
                    ptr--;
                }
                best_k[j] = cur;
            }
        }

        int ans = 2e9;
        bool found = false;
        if (p1.empty()) {
            for (int j = 0; j <= n; j++) {
                int i = best_i[j];
                int k = best_k[j];
                if (i != -1 && k != -1) {
                    ans = min(ans, (k + L2) - i);
                    found = true;
                }
            }
        } else {
            for (int j : pos1) {
                int i = best_i[j];
                int k = best_k[j];
                if (i != -1 && k != -1) {
                    ans = min(ans, (k + L2) - i);
                    found = true;
                }
            }
        }

        return found ? ans : -1;
    }
};
# @lc code=end