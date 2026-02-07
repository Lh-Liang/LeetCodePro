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
        // Iterate through each query
        for (auto& query : queries) {
            if (query[0] == 1) {
                int j = query[1];
                // Flip the character at index j
                s[j] = (s[j] == 'A') ? 'B' : 'A';
            } else if (query[0] == 2) {
                int l = query[1];
                int r = query[2];
                // Calculate minimum deletions needed to make s[l..r] alternating
                int count1 = 0, count2 = 0;
                for (int i = l; i <= r; ++i) {
                    if ((i % 2 == 0 && s[i] != 'A') || (i % 2 != 0 && s[i] != 'B')) {
                        ++count1; // Case where we expect 'A', 'B', 'A', ...
                    } else {
                        ++count2; // Case where we expect 'B', 'A', 'B', ...
                    }
                }
                answer.push_back(min(count1, count2)); // Minimum of two cases gives result for alternating substring. 
            } 
        } 
        return answer; 
    } 
}; 
# @lc code=end