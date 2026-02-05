#
# @lc app=leetcode id=3501 lang=cpp
#
# [3501] Maximize Active Section with Trade II
#
# @lc code=start
class Solution {
public:
    vector<int> maxActiveSectionsAfterTrade(string s, vector<vector<int>>& queries) {
        vector<int> res;
        for (const auto& q : queries) {
            int l = q[0], r = q[1];
            string t = '1' + s.substr(l, r - l + 1) + '1';
            int n = t.size();
            // Count original number of '1's
            int orig = 0;
            for (int i = 1; i < n - 1; ++i) orig += t[i] == '1';
            int max_ones = orig;
            // Find all blocks of '1's surrounded by '0's
            for (int i = 1; i < n - 1;) {
                // Eligible '1' block: t[i-1]=='0', t[i]=='1', ... t[j]=='1', t[j+1]=='0'
                if (t[i-1] == '0' && t[i] == '1') {
                    int j = i;
                    while (j < n - 1 && t[j] == '1') ++j;
                    if (t[j] == '0') {
                        // Simulate converting [i,j-1] to '0's
                        string t2 = t;
                        for (int k = i; k < j; ++k) t2[k] = '0';
                        // Now find all eligible '0' blocks surrounded by '1's
                        for (int x = 1; x < n - 1;) {
                            if (t2[x-1] == '1' && t2[x] == '0') {
                                int y = x;
                                while (y < n - 1 && t2[y] == '0') ++y;
                                if (t2[y] == '1') {
                                    // Simulate converting [x, y-1] to '1's
                                    string t3 = t2;
                                    for (int k = x; k < y; ++k) t3[k] = '1';
                                    int count = 0;
                                    for (int z = 1; z < n - 1; ++z) count += t3[z] == '1';
                                    if (count > max_ones) max_ones = count;
                                }
                                x = y;
                            } else {
                                ++x;
                            }
                        }
                    }
                    i = j;
                } else {
                    ++i;
                }
            }
            res.push_back(max_ones);
        }
        return res;
    }
};
# @lc code=end