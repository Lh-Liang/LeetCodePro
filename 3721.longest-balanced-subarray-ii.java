#
# @lc app=leetcode id=3721 lang=java
#
# [3721] Longest Balanced Subarray II
#
# @lc code=start
import java.util.HashSet;

class Solution {
    public int longestBalanced(int[] nums) {
        int n = nums.length;
        int left = 0, right = 0, maxLen = 0;
        HashSet<Integer> evenSet = new HashSet<>();
        HashSet<Integer> oddSet = new HashSet<>();
        int[] count = new int[100001];
        while (right < n) {
            int num = nums[right];
            count[num]++;
            if (num % 2 == 0) evenSet.add(num);
            else oddSet.add(num);
            while (left <= right && evenSet.size() > oddSet.size()) {
                int lnum = nums[left];
                count[lnum]--;
                if (count[lnum] == 0) {
                    if (lnum % 2 == 0) evenSet.remove(lnum);
                    else oddSet.remove(lnum);
                }
                left++;
            }
            while (left <= right && oddSet.size() > evenSet.size()) {
                int lnum = nums[left];
                count[lnum]--;
                if (count[lnum] == 0) {
                    if (lnum % 2 == 0) evenSet.remove(lnum);
                    else oddSet.remove(lnum);
                }
                left++;
            }
            if (evenSet.size() == oddSet.size()) {
                maxLen = Math.max(maxLen, right - left + 1);
            }
            right++;
        }
        return maxLen;
    }
}
# @lc code=end