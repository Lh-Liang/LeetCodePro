# @lc app=leetcode id=3501 lang=cpp
#
# [3501] Maximize Active Section with Trade II
#
# @lc code=start
class Solution {
public:
    vector<int> maxActiveSectionsAfterTrade(string s, vector<vector<int>>& queries) {
        int n = s.size();
        vector<int> answer;
        for (const auto& q : queries) {
            int l = q[0], r = q[1];
            string t = "1" + s.substr(l, r - l + 1) + "1";
            int m = t.size();
            vector<pair<char, int>> blocks;
            // Count blocks
            int cnt = 1;
            for (int i = 1; i < m; ++i) {
                if (t[i] != t[i-1]) {
                    blocks.push_back({t[i-1], cnt});
                    cnt = 1;
                } else {
                    cnt++;
                }
            }
            blocks.push_back({t[m-1], cnt});
            // Initial number of '1' blocks (excluding first and last augmentation)
            int init = 0;
            for (int i = 0; i < (int)blocks.size(); ++i) {
                if (blocks[i].first == '1') {
                    // Exclude the first and last blocks (the augmentations)
                    if (i != 0 && i != (int)blocks.size()-1)
                        init++;
                }
            }
            int maxActive = init;
            // Try all possible trades
            for (int i = 1; i+1 < (int)blocks.size(); ++i) {
                // Must be a '1' block surrounded by '0's
                if (blocks[i].first == '1' && blocks[i-1].first == '0' && blocks[i+1].first == '0') {
                    // Simulate trade: remove this '1' block, add a '0' block
                    // For the new string, after turning block i to '0', we can turn any '0' block (surrounded by '1's) to '1'
                    // So, try all such '0' blocks
                    for (int j = 1; j+1 < (int)blocks.size(); ++j) {
                        if (blocks[j].first == '0' && blocks[j-1].first == '1' && blocks[j+1].first == '1') {
                            if (j == i || (j == i-1 && blocks[j].first == '0' && blocks[i].first == '1')) continue; // Can't swap the same block just changed
                            // Calculate new number of '1' blocks
                            int cur = init;
                            // Trading away block i removes 1 '1' block
                            cur--;
                            // Trading in block j adds 1 '1' block
                            cur++;
                            maxActive = max(maxActive, cur);
                        }
                    }
                }
            }
            answer.push_back(maxActive);
        }
        return answer;
    }
};
# @lc code=end