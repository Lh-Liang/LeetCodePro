//
// @lc app=leetcode id=3458 lang=cpp
//
// [3458] Select K Disjoint Special Substrings
//

// @lc code=start
class Solution {
public:
    bool maxSubstringLength(string s, int k) {
        int n = s.length();
        
        if (k == 0) return true;
        
        // Find first and last occurrence of each character
        vector<int> first(26, -1), last(26, -1);
        for (int i = 0; i < n; i++) {
            int c = s[i] - 'a';
            if (first[c] == -1) first[c] = i;
            last[c] = i;
        }
        
        // For each character, find the minimal special substring starting from it
        vector<pair<int, int>> intervals;
        for (int c = 0; c < 26; c++) {
            if (first[c] == -1) continue;
            
            int left = first[c], right = last[c];
            bool valid = true;
            
            for (int i = left; i <= right && valid; i++) {
                int cc = s[i] - 'a';
                if (first[cc] < left) {
                    valid = false;
                }
                right = max(right, last[cc]);
            }
            
            if (!valid) continue;
            if (left == 0 && right == n - 1) continue;
            
            intervals.push_back({left, right});
        }
        
        // Greedy interval scheduling - select non-overlapping intervals
        // Sort by end time
        sort(intervals.begin(), intervals.end(), [](auto& a, auto& b) {
            return a.second < b.second;
        });
        
        int count = 0;
        int lastEnd = -1;
        for (auto& [l, r] : intervals) {
            if (l > lastEnd) {
                count++;
                lastEnd = r;
            }
        }
        
        return count >= k;
    }
};
// @lc code=end