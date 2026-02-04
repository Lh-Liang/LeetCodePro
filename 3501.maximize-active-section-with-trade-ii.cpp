#
# @lc app=leetcode id=3501 lang=cpp
#
# [3501] Maximize Active Section with Trade II
#

# @lc code=start
class Solution {
public:
    vector<int> maxActiveSectionsAfterTrade(string s, vector<vector<int>>& queries) {
        vector<int> results;
        for (const auto& query : queries) {
            int li = query[0], ri = query[1];
            string t = "1" + s.substr(li, ri - li + 1) + "1"; // Augment the substring with 1s
            int max_active = 0;
            vector<int> zero_blocks, one_blocks;
            
            // Detect blocks and calculate initial active count
            int i = 0;
            while (i < t.size()) {
                int j = i;
                while (j < t.size() && t[j] == t[i]) j++;
                if (t[i] == '0') zero_blocks.push_back(j - i);
                else one_blocks.push_back(j - i);
                i = j;
            }

            // Calculate initial active sections count without any trade
            int current_active = 0;
            for (int len : one_blocks) current_active += len;
            max_active = current_active;

            // Attempt trades and calculate maximum active sections
            for (int z : zero_blocks) { // Consider each block of zeros that can be flipped to ones
                // Ensure there is at least one block of ones that can be flipped to zeros first
                if (one_blocks.size() > 1) { 
                    max_active = max(max_active, current_active + z);
                }
            }
            results.push_back(max_active);
        }
        return results;
    }
};
# @lc code=end