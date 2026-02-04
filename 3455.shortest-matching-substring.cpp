#
# @lc app=leetcode id=3455 lang=cpp
#
# [3455] Shortest Matching Substring
#
# @lc code=start
class Solution {
public:
    int shortestMatchingSubstring(string s, string p) {
        // Step 1: Extract the positions of '*'
        vector<int> starPos;
        for (int i = 0; i < p.size(); ++i) {
            if (p[i] == '*') starPos.push_back(i);
        }
        if (starPos.size() != 2) return -1; // per problem constraint
        int n = s.size(), m = p.size();
        string pre = p.substr(0, starPos[0]);
        string mid = p.substr(starPos[0]+1, starPos[1]-starPos[0]-1);
        string suf = p.substr(starPos[1]+1);
        
        // Special case: both wildcards, pattern is "**"
        if (m == 2 && p == "**") return 0;
        int res = INT_MAX;
        // Precompute all prefix match indices
        vector<int> pre_idx;
        for (int i = 0; i+pre.size() <= n; ++i) {
            if (s.substr(i, pre.size()) == pre) pre_idx.push_back(i);
        }
        // Precompute all suffix match indices
        vector<int> suf_idx;
        for (int i = 0; i+suf.size() <= n; ++i) {
            if (s.substr(i, suf.size()) == suf) suf_idx.push_back(i);
        }
        // For each prefix, find a valid suffix after it
        for (int i : pre_idx) {
            int pre_end = i + pre.size();
            for (int j : suf_idx) {
                int suf_start = j;
                int suf_end = j + suf.size();
                if (suf_end <= n && pre_end <= suf_start) {
                    // The candidate substring: s[i .. suf_end-1]
                    int mid_len = mid.size();
                    bool mid_ok = false;
                    if (mid.empty()) {
                        mid_ok = true;
                    } else {
                        // Search for mid between pre_end and suf_start
                        for (int k = pre_end; k+mid_len <= suf_start; ++k) {
                            if (s.substr(k, mid_len) == mid) {
                                mid_ok = true;
                                break;
                            }
                        }
                    }
                    if (mid_ok) {
                        res = min(res, suf_end - i);
                        break; // No need to check further suffixes for this prefix
                    }
                }
            }
        }
        return res == INT_MAX ? -1 : res;
    }
};
# @lc code=end