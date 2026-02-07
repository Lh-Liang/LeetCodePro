#
# @lc app=leetcode id=3445 lang=cpp
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#
# @lc code=start
class Solution {
public:
    int maxDifference(string s, int k) {
        int n = s.size();
        unordered_map<char, int> freq;
        int maxDiff = INT_MIN;
        int start = 0;
        
        for (int end = 0; end < n; ++end) {
            freq[s[end]]++;
            
            // When we have a valid window of at least size k
            if (end - start + 1 >= k) {
                // Check for odd/even frequency characters within this window
                int oddMax = INT_MIN, evenMax = INT_MIN;
                for (auto &p : freq) {
                    if (p.second % 2 == 1) { // odd frequency
                        oddMax = max(oddMax, p.second);
                    } else if (p.second > 0) { // non-zero even frequency
                        evenMax = max(evenMax, p.second);
                    }
                }
                
                // Compute potential max difference
                if (oddMax != INT_MIN && evenMax != INT_MIN) {
                    maxDiff = max(maxDiff, oddMax - evenMax);
                }
                
                // Slide the window by reducing start point
                freq[s[start]]--;
                if (freq[s[start]] == 0) {
                    freq.erase(s[start]);
                }
                start++;
            }
        }
        
        return maxDiff == INT_MIN ? -1 : maxDiff;
    }
};
# @lc code=end