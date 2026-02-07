#
# @lc app=leetcode id=3777 lang=cpp
#
# [3777] Minimum Deletions to Make Alternating Substring
#

# @lc code=start
class Solution {
public:
    vector<int> minDeletions(string s, vector<vector<int>>& queries) {
        vector<int> answer;
        for (const auto& query : queries) {
            if (query[0] == 1) { // Flip operation
                int j = query[1];
                s[j] = (s[j] == 'A') ? 'B' : 'A';
            } else if (query[0] == 2) { // Compute deletions for alternating substring
                int l = query[1], r = query[2];
                int deletionsAB = 0, deletionsBA = 0;
                for (int i = l; i < r; ++i) {
                    if ((i % 2 == l % 2 && s[i] != 'A') || (i % 2 != l % 2 && s[i] != 'B')) {
                        ++deletionsAB;
                    }
                    if ((i % 2 == l % 2 && s[i] != 'B') || (i % 2 != l % 2 && s[i] != 'A')) {
                        ++deletionsBA;
                    }
                }
                answer.push_back(min(deletionsAB, deletionsBA));
            }
        }
        return answer;
    }
};
# @lc code=end