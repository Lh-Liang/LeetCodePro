#
# @lc app=leetcode id=3501 lang=java
#
# [3501] Maximize Active Section with Trade II
#
# @lc code=start
import java.util.*;
class Solution {
    public List<Integer> maxActiveSectionsAfterTrade(String s, int[][] queries) {
        List<Integer> ans = new ArrayList<>();
        for (int[] q : queries) {
            int l = q[0], r = q[1];
            String sub = s.substring(l, r + 1);
            StringBuilder t = new StringBuilder();
            t.append('1'); t.append(sub); t.append('1');
            int n = t.length();
            char[] arr = t.toString().toCharArray();
            // Find all '1' blocks
            List<int[]> oneBlocks = new ArrayList<>();
            int i = 0;
            while (i < n) {
                if (arr[i] == '1') {
                    int j = i;
                    while (j < n && arr[j] == '1') j++;
                    oneBlocks.add(new int[]{i, j - 1});
                    i = j;
                } else {
                    i++;
                }
            }
            // Initial number of '1' sections in substring (excluding the augmentation)
            int count = 0;
            for (int[] block : oneBlocks) {
                int left = block[0], right = block[1];
                if (left != 0 && right != n - 1) {
                    count++;
                }
            }
            int maxCount = count;
            // For each possible '1' block surrounded by '0's, try trading
            for (int idx = 1; idx < oneBlocks.size() - 1; idx++) {
                int[] block = oneBlocks.get(idx);
                int left = block[0], right = block[1];
                // Check if this block is surrounded by '0's
                if (arr[left - 1] == '0' && arr[right + 1] == '0') {
                    // Simulate removal
                    // Create a copy for simulation
                    char[] temp = Arrays.copyOf(arr, n);
                    for (int k = left; k <= right; k++) temp[k] = '0';
                    // Now find all '0' blocks surrounded by '1's
                    i = 0;
                    List<int[]> zeroBlocks = new ArrayList<>();
                    while (i < n) {
                        if (temp[i] == '0') {
                            int j = i;
                            while (j < n && temp[j] == '0') j++;
                            if (i > 0 && j < n && temp[i - 1] == '1' && temp[j] == '1') {
                                zeroBlocks.add(new int[]{i, j - 1});
                            }
                            i = j;
                        } else {
                            i++;
                        }
                    }
                    // Try converting each zero block and count
                    for (int[] zblock : zeroBlocks) {
                        char[] trial = Arrays.copyOf(temp, n);
                        for (int k = zblock[0]; k <= zblock[1]; k++) trial[k] = '1';
                        // Count new '1' sections
                        int c = 0;
                        for (int m = 1; m < n - 1; ) {
                            if (trial[m] == '1') {
                                int end = m;
                                while (end < n - 1 && trial[end] == '1') end++;
                                c++;
                                m = end;
                            } else {
                                m++;
                            }
                        }
                        maxCount = Math.max(maxCount, c);
                    }
                }
            }
            ans.add(maxCount);
        }
        return ans;
    }
}
# @lc code=end