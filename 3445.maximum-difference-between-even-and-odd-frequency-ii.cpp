#
# @lc app=leetcode id=3445 lang=cpp
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#

# @lc code=start
class Solution {
public:
    int maxDifference(string s, int k) {
        int maxDiff = INT_MIN;
        unordered_map<char, int> freq;
        // Initialize sliding window
        for (int i = 0; i < s.size(); ++i) {
            ++freq[s[i]];
            if (i >= k - 1) { // Only consider substrings of at least size k
                int oddMax = INT_MIN, evenMax = INT_MIN;
                // Calculate current max difference between odd and even frequencies
                for (auto &[char, count] : freq) {
                    if (count % 2 == 1) { // Odd frequency
                        oddMax = max(oddMax, count);
                    } else if (count > 0 && count % 2 == 0) { // Even non-zero frequency
                        evenMax = max(evenMax, count);
                    }
                }
                if (oddMax != INT_MIN && evenMax != INT_MIN) { // Valid pair found
                    maxDiff = max(maxDiff, oddMax - evenMax);
                }
                // Slide window: remove leftmost character from consideration
                --freq[s[i - k + 1]];
            }
        }
        return maxDiff == INT_MIN ? -1 : maxDiff; // Return -1 if no valid difference found
    } 
}; 
# @lc code=end