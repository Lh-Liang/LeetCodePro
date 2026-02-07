#
# @lc app=leetcode id=3458 lang=cpp
#
# [3458] Select K Disjoint Special Substrings
#

# @lc code=start
class Solution {
public:
    bool maxSubstringLength(string s, int k) {
        unordered_map<char, vector<int>> charPositions;
        for (int i = 0; i < s.size(); ++i) {
            charPositions[s[i]].push_back(i);
        }
        int possibleSubstrings = 0;
        for (const auto& entry : charPositions) {
            if (entry.second.size() == 1) { // Unique character occurrence
                ++possibleSubstrings;
            } else { // Check if all occurrences form a single segment
                bool isSegment = true;
                for (int j = 1; j < entry.second.size(); ++j) {
                    if (entry.second[j] != entry.second[j - 1] + 1) {
                        isSegment = false;
                        break;
                    }
                }
                if (isSegment) { ++possibleSubstrings; }
            }
        }
        return possibleSubstrings >= k; // Check if we can make at least k such special substrings. 
    } 
}; 
# @lc code=end