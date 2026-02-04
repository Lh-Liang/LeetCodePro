#
# @lc app=leetcode id=3455 lang=cpp
#
# [3455] Shortest Matching Substring
#

# @lc code=start
class Solution {
public:
    int shortestMatchingSubstring(string s, string p) {
        size_t firstStar = p.find('*');
        size_t lastStar = p.rfind('*');
        string pre = p.substr(0, firstStar);
        string mid = p.substr(firstStar + 1, lastStar - firstStar - 1);
        string post = p.substr(lastStar + 1);
        int minLen = INT_MAX;
        
        for (size_t i = 0; i <= s.size() - pre.size(); ++i) {
            if (s.compare(i, pre.size(), pre) == 0) {
                size_t midPos = s.find(mid, i + pre.size());
                if (midPos != string::npos) {
                    size_t postPos = s.find(post, midPos + mid.size());
                    if (postPos != string::npos) {
                        minLen = min(minLen, static_cast<int>(postPos + post.size() - i));
                    }
                }
            }
        }
        return minLen == INT_MAX ? -1 : minLen;
    }
};
# @lc code=end