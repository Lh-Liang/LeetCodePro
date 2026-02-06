#
# @lc app=leetcode id=3575 lang=java
#
# [3575] Maximum Good Subtree Score
#
# @lc code=start
class Solution {
    private static final int MOD = 1000000007;
    public int goodSubtreeSum(int[] vals, int[] par) {
        int n = vals.length;
        List<Integer>[] tree = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            tree[i] = new ArrayList<>();
        }
        for (int i = 1; i < n; i++) {
            tree[par[i]].add(i);
        }
        int[] maxScore = new int[n];
        dfs(0, vals, tree, maxScore);
        long totalScore = 0;
        for (int score : maxScore) {
            totalScore = (totalScore + score) % MOD;
        }
        return (int) totalScore;
    }
    private int dfs(int node, int[] vals, List<Integer>[] tree, int[] maxScore) {
        int currentNodeValue = vals[node];
        int currentBitMask = getBitmask(currentNodeValue); // Convert value to bitmask representation of digits. 
        long currentSum = currentNodeValue; 
        for (int child : tree[node]) { 
            int childBitmaskSum = dfs(child, vals, tree, maxScore); 
            if ((currentBitMask & childBitmaskSum) == 0) { 
                // Combine if there are no common digits. 
                currentBitMask |= childBitmaskSum >> 10; 
                currentSum += childBitmaskSum & ((1L << 10) - 1); 
            } 
        } 
        maxScore[node] = (int)(currentSum % MOD); 
        return ((currentBitMask << 10) | (int)(currentSum % MOD)); // Return combined bitmask with sum encoded. 
    } 
    private int getBitmask(int value) { 
        boolean[] seenDigits = new boolean[10]; ​// Track seen digits. ​while (value > 0) { ​int digit = value % 10; if (seenDigits[digit]) return -1; // Invalid if digit repeats. seenDigits[digit] = true; value /= 10; } int bitmask = 0;for (int d = 0; d < 10; d++) {if (seenDigits[d]) bitmask |= (1 << d);}return bitmask;} }// @lc code=end