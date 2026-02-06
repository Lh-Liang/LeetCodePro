#
# @lc app=leetcode id=3445 lang=java
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#

# @lc code=start
class Solution {
    public int maxDifference(String s, int k) {
        int maxDiff = Integer.MIN_VALUE;
        for (int start = 0; start <= s.length() - k; start++) {
            int[] freq = new int[10]; // Digits 0-9
            for (int end = start; end < s.length(); end++) {
                freq[s.charAt(end) - '0']++;
                if (end - start + 1 >= k) {
                    int oddMax = Integer.MIN_VALUE;
                    int evenMin = Integer.MAX_VALUE;
                    for (int i = 0; i < freq.length; i++) {
                        if (freq[i] > 0) { // Non-zero check
                            if (freq[i] % 2 == 1) { // Odd frequency check
                                oddMax = Math.max(oddMax, freq[i]);
                            } else { // Even frequency check
                                evenMin = Math.min(evenMin, freq[i]);
                            }
                        }
                    }
                    if (oddMax != Integer.MIN_VALUE && evenMin != Integer.MAX_VALUE) { // Valid pair check
                        maxDiff = Math.max(maxDiff, oddMax - evenMin);
                    }
                }
            }
        }
        return maxDiff == Integer.MIN_VALUE ? -1 : maxDiff; // Return -1 if no valid pair found. 
    } 
}
# @lc code=end