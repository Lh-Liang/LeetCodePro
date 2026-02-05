#
# @lc app=leetcode id=3445 lang=java
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#

# @lc code=start
class Solution {
    public int maxDifference(String s, int k) {
        int n = s.length();
        int maxDiff = Integer.MIN_VALUE;
        // Only 5 digits: '0' to '4'
        for (int a = 0; a < 5; a++) {
            for (int b = 0; b < 5; b++) {
                if (a == b) continue;
                int[] freq = new int[5];
                // Initialize first window of size k
                for (int i = 0; i < k; i++) {
                    freq[s.charAt(i) - '0']++;
                }
                // Check initial window
                if (freq[a] % 2 == 1 && freq[b] > 0 && freq[b] % 2 == 0) {
                    maxDiff = Math.max(maxDiff, freq[a] - freq[b]);
                }
                // Slide the window
                for (int right = k; right < n; right++) {
                    freq[s.charAt(right) - '0']++;
                    freq[s.charAt(right - k) - '0']--;
                    if (freq[a] % 2 == 1 && freq[b] > 0 && freq[b] % 2 == 0) {
                        maxDiff = Math.max(maxDiff, freq[a] - freq[b]);
                    }
                }
                // Now handle substrings longer than k
                // For each window size from k+1 to n
                for (int window = k + 1; window <= n; window++) {
                    // Reset frequencies
                    freq = new int[5];
                    for (int i = 0; i < window; i++) {
                        freq[s.charAt(i) - '0']++;
                    }
                    if (freq[a] % 2 == 1 && freq[b] > 0 && freq[b] % 2 == 0) {
                        maxDiff = Math.max(maxDiff, freq[a] - freq[b]);
                    }
                    for (int right = window; right < n; right++) {
                        freq[s.charAt(right) - '0']++;
                        freq[s.charAt(right - window) - '0']--;
                        if (freq[a] % 2 == 1 && freq[b] > 0 && freq[b] % 2 == 0) {
                            maxDiff = Math.max(maxDiff, freq[a] - freq[b]);
                        }
                    }
                }
            }
        }
        return maxDiff == Integer.MIN_VALUE ? -1 : maxDiff;
    }
}
# @lc code=end