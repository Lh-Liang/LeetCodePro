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
        for (const auto& q : queries) {
            if (q[0] == 1) {
                int j = q[1];
                s[j] = (s[j] == 'A' ? 'B' : 'A');
            } else {
                int l = q[1], r = q[2];
                int deletions = 0;
                for (int i = l; i < r; ++i) {
                    if (s[i] == s[i+1]) ++deletions;
                }
                answer.push_back(deletions);
            }
        }
        return answer;
    }
};
# @lc code=end