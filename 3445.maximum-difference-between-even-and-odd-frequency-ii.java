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
        boolean found = false;
        // Enumerate all digit pairs (a, b), a != b
        for (int a = 0; a < 5; a++) {
            for (int b = 0; b < 5; b++) {
                if (a == b) continue;
                int[] freq = new int[5];
                int left = 0;
                for (int right = 0; right < n; right++) {
                    freq[s.charAt(right) - '0']++;
                    // Slide window to maintain length at least k
                    while (right - left + 1 > k) {
                        freq[s.charAt(left) - '0']--;
                        left++;
                    }
                    if (right - left + 1 >= k) {
                        int fa = freq[a];
                        int fb = freq[b];
                        if (fa % 2 == 1 && fb > 0 && fb % 2 == 0) {
                            maxDiff = Math.max(maxDiff, fa - fb);
                            found = true;
                        }
                    }
                }
            }
        }
        return found ? maxDiff : -1;
    }
}
# @lc code=end