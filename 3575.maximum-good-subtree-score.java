#
# @lc app=leetcode id=3575 lang=java
#
# [3575] Maximum Good Subtree Score
#

# @lc code=start
import java.util.*;

class Solution {
    private static final int MOD = 1000000007;
    private List<Integer>[] tree;
    private int[] vals;
    
    public int goodSubtreeSum(int[] vals, int[] par) {
        int n = vals.length;
        this.vals = vals;
        tree = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            tree[i] = new ArrayList<>();
        }
        for (int i = 1; i < n; i++) {
            tree[par[i]].add(i);
        }
        
        long[] maxScore = new long[n];
        dfs(0, maxScore);
        
        long totalScore = 0;
        for (long score : maxScore) {
            totalScore = (totalScore + score) % MOD;
        }
        return (int) totalScore;
    }
    
    private void dfs(int node, long[] maxScore) {
        boolean[] usedDigits = new boolean[10]; // To track used digits in subtree values.
        maxScore[node] = dfsHelper(node, usedDigits); // Calculate score for this subtree. 
    }
    
    private long dfsHelper(int node, boolean[] usedDigits) {
        long currSum = vals[node]; // Start with current node value.
        if (!addDigits(vals[node], usedDigits)) return 0; // If cannot add due to digit conflict.
        for (int child : tree[node]) { 
            currSum += dfsHelper(child, usedDigits); // Sum up valid scores from children.
            currSum %= MOD; // Apply modulo to prevent overflow.
 removeDigits(vals[node], usedDigits); // Backtrack on digits.
 return currSum; }/ Adds digits of value if not yet used in subtree. Returns false if conflict occurs.\u21e8\u21e8boolean addDigits(int value, boolean[] usedDigits) { \u21e8\u21e8while (value > 0) { \u21e8\u21e8int digit = value % 10; \u21e8\u21e8if \(usedDigits[digit]) return false; \ u\21e8\ u\21e8usedDigits[digit] = true; \ u\21e8\ u\21e8value /= 10;} \ u\21e8return true;} \ removeDigits(int value, boolean[] usedDigits) { while (value > 0) { int digit = value % 10; usedDigits[digit] = false; value /= 10;} }