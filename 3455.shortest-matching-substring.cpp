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
    vector<int> kmp(const string& s, const string& p) {
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
        int firstStar = p.find('*');
        int secondStar = p.find('*', firstStar + 1);
        
        string A = p.substr(0, firstStar);
        string B = p.substr(firstStar + 1, secondStar - firstStar - 1);
        string C = p.substr(secondStar + 1);
        
        vector<int> vA = kmp(s, A);
        vector<int> vB = kmp(s, B);
        vector<int> vC = kmp(s, C);
        
        if (!A.empty() && vA.empty()) return -1;
        if (!B.empty() && vB.empty()) return -1;
        if (!C.empty() && vC.empty()) return -1;
        
        int ans = INT_MAX;
        
        if (!B.empty()) {
            for (int j : vB) {
                int i = -1;
                if (A.empty()) {
                    i = j;
                } else {
                    auto it = upper_bound(vA.begin(), vA.end(), j - (int)A.length());
                    if (it != vA.begin()) {
                        i = *prev(it);
                    }
                }
                
                int k = -1;
                if (C.empty()) {
                    k = j + (int)B.length();
                } else {
                    auto it = lower_bound(vC.begin(), vC.end(), j + (int)B.length());
                    if (it != vC.end()) {
                        k = *it;
                    }
                }
                
                if (i != -1 && k != -1) {
                    ans = min(ans, k + (int)C.length() - i);
                }
            }
        } else {
            if (!A.empty() && !C.empty()) {
                for (int i : vA) {
                    auto it = lower_bound(vC.begin(), vC.end(), i + (int)A.length());
                    if (it != vC.end()) {
                        int k = *it;
                        ans = min(ans, k + (int)C.length() - i);
                    }
                }
            } else if (!A.empty()) {
                ans = A.length();
            } else if (!C.empty()) {
                ans = C.length();
            } else {
                ans = 0;
            }
        }
        
        return (ans == INT_MAX) ? -1 : ans;
    }
};
# @lc code=end