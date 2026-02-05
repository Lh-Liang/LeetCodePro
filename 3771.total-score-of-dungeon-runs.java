#
# @lc app=leetcode id=3771 lang=java
#
# [3771] Total Score of Dungeon Runs
#

# @lc code=start
import java.util.*;
class Solution {
    public long totalScore(int hp, int[] damage, int[] requirement) {
        int n = damage.length;
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; ++i) {
            prefix[i + 1] = prefix[i] + damage[i];
        }
        // prefix[0..n] is sorted, so we can binary search
        long total = 0;
        for (int i = 0; i < n; ++i) {
            long threshold = hp - requirement[i] + prefix[i + 1];
            // Find the rightmost j-1 <= i such that prefix[j-1] <= threshold
            // i.e., count of j in [1, i+1] with prefix[j-1] <= threshold
            int left = 0, right = i + 1;
            int pos = -1;
            while (left <= right) {
                int mid = left + (right - left) / 2;
                if (prefix[mid] <= threshold) {
                    pos = mid;
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
            // The number of valid j is pos in [0, i], i.e., pos - 0 + 1 = pos + 1
            if (pos >= 0) {
                total += Math.min(pos + 1, i + 1);
            }
        }
        return total;
    }
}
# @lc code=end