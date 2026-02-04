#
# @lc app=leetcode id=3445 lang=cpp
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#

# @lc code=start
class Solution {
public:
    int maxDifference(string s, int k) {
        int max_diff = -1; // Initialize maximum difference as -1 (impossible case)
        int n = s.length();
        for (int start = 0; start <= n - k; ++start) {
            vector<int> freq(5, 0); // Initialize frequency vector for digits '0' to '4'
            for (int end = start; end < n; ++end) {
                freq[s[end] - '0']++;
                if (end - start + 1 >= k) { // Only consider substrings of at least length k
                    int max_odd = INT_MIN, min_even = INT_MAX;
                    for (int num = 0; num <= 4; ++num) {
                        if (freq[num] % 2 == 1) { // Odd frequency check
                            max_odd = max(max_odd, freq[num]);
                        } else if (freq[num] > 0) { // Even and non-zero frequency check
                            min_even = min(min_even, freq[num]);
                        }
                    }
                    if (max_odd != INT_MIN && min_even != INT_MAX) { // Valid odd/even found in substring
                        max_diff = max(max_diff, max_odd - min_even);
                    }
                }
            }
        }
        return max_diff; // Return maximum difference found or -1 if none valid found. 
    }
}; 
# @lc code=end