#
# @lc app=leetcode id=3455 lang=cpp
#
# [3455] Shortest Matching Substring
#

# @lc code=start
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>

using namespace std;

class Solution {
public:
    vector<int> findOccurrences(const string& text, const string& pattern) {
        int n_p = pattern.size();
        int n_s = text.size();
        if (n_p == 0) {
            vector<int> res(n_s + 1);
            iota(res.begin(), res.end(), 0);
            return res;
        }

        string combined = pattern + "#" + text;
        int m = combined.size();
        vector<int> z(m);
        int l = 0, r = 0;
        for (int i = 1; i < m; i++) {
            if (i <= r) z[i] = min(r - i + 1, z[i - l]);
            while (i + z[i] < m && combined[z[i]] == combined[i + z[i]]) z[i]++;
            if (i + z[i] - 1 > r) {
                l = i;
                r = i + z[i] - 1;
            }
        }

        vector<int> res;
        for (int i = n_p + 1; i < m; i++) {
            if (z[i] == n_p) {
                res.push_back(i - (n_p + 1));
            }
        }
        return res;
    }

    int shortestMatchingSubstring(string s, string p) {
        size_t firstStar = p.find('*');
        size_t secondStar = p.find('*', firstStar + 1);

        string p1 = p.substr(0, firstStar);
        string p2 = p.substr(firstStar + 1, secondStar - firstStar - 1);
        string p3 = p.substr(secondStar + 1);

        vector<int> V1 = findOccurrences(s, p1);
        vector<int> V2 = findOccurrences(s, p2);
        vector<int> V3 = findOccurrences(s, p3);

        if (V1.empty() || V2.empty() || V3.empty()) return -1;

        int min_len = 2e9;
        int i_ptr = 0;
        int k_ptr = 0;

        for (int j : V2) {
            // Find largest i in V1 such that i <= j - p1.size()
            while (i_ptr < V1.size() && V1[i_ptr] <= j - (int)p1.size()) {
                i_ptr++;
            }
            if (i_ptr == 0) continue;
            int i = V1[i_ptr - 1];

            // Find smallest k in V3 such that k >= j + p2.size()
            while (k_ptr < V3.size() && V3[k_ptr] < j + (int)p2.size()) {
                k_ptr++;
            }
            if (k_ptr == V3.size()) continue;
            int k = V3[k_ptr];

            min_len = min(min_len, (k + (int)p3.size()) - i);
        }

        return (min_len > (int)s.size()) ? -1 : min_len;
    }
};
# @lc code=end