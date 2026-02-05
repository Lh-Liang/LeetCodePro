# @lc app=leetcode id=3562 lang=java
#
# [3562] Maximum Profit from Trading Stocks with Discounts
#
# @lc code=start
import java.util.*;
class Solution {
    public int maxProfit(int n, int[] present, int[] future, int[][] hierarchy, int budget) {
        // Convert hierarchy into adjacency list for traversal
        List<Integer>[] tree = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            tree[i] = new ArrayList<>();
        }
        for (int[] pair : hierarchy) {
            tree[pair[0]].add(pair[1]);
        }
        
        // DP array
        int[][] dp = new int[n + 1][budget + 1];
        for (int i = 0; i <= n; i++) {
            Arrays.fill(dp[i], -1); // Initialize dp with uncomputed state
        }
        
        return dfs(1, budget, present, future, tree, dp);
    }
    
    private int dfs(int empId, int budget,
                    int[] present, int[] future,
                    List<Integer>[] tree,
                    int[][] dp) {
        if (dp[empId][budget] != -1) return dp[empId][budget];

        // Max profit without buying current employee's stock
        int maxProfit = 0;

        // Calculate direct profit if this employee buys their stock
        int cost = present[empId - 1];
        if (budget >= cost) {
            maxProfit = Math.max(maxProfit,
future[empId - 1] - cost + dfsSubordinates(empId, budget - cost, present, future, tree));	}	// Explore subordinates without affecting them (no discount)	for (int sub : tree[empId]) {		maxProfit += dfs(sub,budget,present,future);}	dp[empId][budget]=maxProfit;	return maxProfit;	}	private int dfsSubordinates(int empId,int budget,int[] present,int[] future,List<Integer>[] tree){	int maxProfit=0;	for(int sub:tree[empId]){		// Check if discount applies		int discountedCost=present[sub-1]/2;		if(budget>=discountedCost){			maxProfit+=Math.max(	future[sub-1]-discountedCost+dfsSubordinates(sub,budget-discountedCost,present,future),dfs(sub,budget,present,future));	}	}	dp table will be filled through a DFS traversal handling discounts for subordinates.	return maxProfit;	}	}	# @lc code=end