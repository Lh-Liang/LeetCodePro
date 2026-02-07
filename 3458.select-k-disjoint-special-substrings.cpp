#
# @lc app=leetcode id=3458 lang=cpp
#
# [3458] Select K Disjoint Special Substrings
#
# @lc code=start
class Solution {
public:
    bool maxSubstringLength(string s, int k) {
        if (k == 0) return true;
        unordered_map<char, int> charCount;
        for (char c : s) {
            charCount[c]++;
        }

        vector<pair<int, int>> potentialSegments;
        unordered_set<char> usedChars;
        int n = s.length();

        for (int start = 0; start < n; ++start) {
            if (usedChars.find(s[start]) != usedChars.end()) continue;
            unordered_set<char> currentSegmentChars;
            int end = start;
            bool isValidSegment = true;
            
            while (end < n && isValidSegment) {
                char currentChar = s[end];
                if (charCount[currentChar] == 1 && currentSegmentChars.find(currentChar) == currentSegmentChars.end()) {
                    currentSegmentChars.insert(currentChar);
                    end++;
                } else if (currentSegmentChars.find(currentChar) != currentSegmentChars.end()) {
                    // Character repeats within the current segment, so invalidate it.
                    isValidSegment = false;
                } else {
                    break; // Character appears outside intended segment.
                }
            }
            
            if (isValidSegment && !currentSegmentChars.empty()) {
                potentialSegments.push_back({start, end - 1});
                usedChars.insert(currentSegmentChars.begin(), currentSegmentChars.end());
            }
        }

        return potentialSegments.size() >= k;
    }
};
# @lc code=end