#
# @lc app=leetcode id=3777 lang=cpp
#
# [3777] Minimum Deletions to Make Alternating Substring
#

# @lc code=start
class Solution {
public:
    vector<int> minDeletions(string s, vector<vector<int>>& queries) {
        vector<int> result;
        for (auto& query : queries) {
            if (query[0] == 1) {
                // Flip the character at index j
                int j = query[1];
                s[j] = (s[j] == 'A') ? 'B' : 'A';
            } else if (query[0] == 2) {
                // Calculate minimum deletions for alternating substring
                int l = query[1], r = query[2];
                int deletions1 = 0, deletions2 = 0;
                char expectedChar1 = 'A', expectedChar2 = 'B';
                for (int i = l; i <= r; ++i) {
                    if (s[i] != expectedChar1) ++deletions1; // Count mismatches for pattern starting with 'A'
                    if (s[i] != expectedChar2) ++deletions2; // Count mismatches for pattern starting with 'B'
                    // Toggle expected characters for next position
                    expectedChar1 = (expectedChar1 == 'A') ? 'B' : 'A';
                    expectedChar2 = (expectedChar2 == 'A') ? 'B' : 'A';
                }
                result.push_back(min(deletions1, deletions2)); // Choose minimal deletions required
            }
        }
        return result;
    }
};
# @lc code=end