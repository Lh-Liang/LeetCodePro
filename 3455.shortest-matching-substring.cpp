#
# @lc app=leetcode id=3455 lang=cpp
#
# [3455] Shortest Matching Substring
#
# @lc code=start
#include <vector>
#include <string>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    // Standard KMP to find all starting positions of pattern p in string s
    vector<int> findAll(const string& s, const string& p) {
        if (p.empty()) return {};
        int n = s.size(), m = p.size();
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
        int firstStar = p.find('*');
        int secondStar = p.find('*', firstStar + 1);

        string p1 = p.substr(0, firstStar);
        string p2 = p.substr(firstStar + 1, secondStar - firstStar - 1);
        string p3 = p.substr(secondStar + 1);

        // Find all occurrences of the three parts
        vector<int> L1 = findAll(s, p1);
        vector<int> L2 = findAll(s, p2);
        vector<int> L3 = findAll(s, p3);

        // If a non-empty part is not found, no match is possible
        if (!p1.empty() && L1.empty()) return -1;
        if (!p2.empty() && L2.empty()) return -1;
        if (!p3.empty() && L3.empty()) return -1;

        int minLen = INT_MAX;

        if (!p2.empty()) {
            int ptr1 = 0, ptr3 = 0;
            int best_i1 = -1;
            // For each occurrence of the middle part p2
            for (int i2 : L2) {
                // Find the latest i1 that ends before or at i2
                if (p1.empty()) {
                    best_i1 = i2;
                } else {
                    while (ptr1 < (int)L1.size() && L1[ptr1] <= i2 - (int)p1.size()) {
                        best_i1 = L1[ptr1];
                        ptr1++;
                    }
                }

                if (best_i1 == -1) continue;

                // Find the earliest i3 that starts after or at the end of p2
                int current_i3 = -1;
                if (p3.empty()) {
                    current_i3 = i2 + (int)p2.size();
                } else {
                    while (ptr3 < (int)L3.size() && L3[ptr3] < i2 + (int)p2.size()) {
                        ptr3++;
                    }
                    if (ptr3 < (int)L3.size()) {
                        current_i3 = L3[ptr3];
                    }
                }

                if (current_i3 != -1) {
                    minLen = min(minLen, (int)(current_i3 + (int)p3.size() - best_i1));
                }
            }
        } else {
            // Case where p2 is empty (pattern is p1**p3)
            if (p1.empty() && p3.empty()) return 0;
            if (p1.empty()) return p3.size();
            if (p3.empty()) return p1.size();

            int ptr3 = 0;
            for (int i1 : L1) {
                while (ptr3 < (int)L3.size() && L3[ptr3] < i1 + (int)p1.size()) {
                    ptr3++;
                }
                if (ptr3 < (int)L3.size()) {
                    minLen = min(minLen, (int)(L3[ptr3] + (int)p3.size() - i1));
                }
            }
        }

        return minLen == INT_MAX ? -1 : minLen;
    }
};
# @lc code=end