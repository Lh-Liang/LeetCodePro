# @lc app=leetcode id=3530 lang=java
#
# [3530] Maximum Profit from Valid Topological Order in DAG
#
# @lc code=start
import java.util.*;

class Solution {
    public int maxProfit(int n, int[][] edges, int[] score) {
        // Step 1: Build graph and calculate in-degrees
        List<Integer>[] graph = new ArrayList[n];
        int[] inDegree = new int[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int[] edge : edges) {
            graph[edge[0]].add(edge[1]);
            inDegree[edge[1]]++;
        }

        // Step 2: Backtrack to find maximum profit by exploring all topological sorts
        return backtrack(new ArrayList<>(), new boolean[n], inDegree, graph, score);
    }

    private int backtrack(List<Integer> currentOrder, boolean[] visited, int[] inDegree, List<Integer>[] graph, int[] score) {
        if (currentOrder.size() == visited.length) {
            // Calculate profit for this order
            return calculateProfit(currentOrder, score);
        }

        int maxProfit = 0;
        for (int i = 0; i < visited.length; i++) {
            if (!visited[i] && inDegree[i] == 0) {
                // Choose node i and add it to currentOrder
                visited[i] = true;
                currentOrder.add(i);
                // Temporarily decrease in-degree of neighbors
                for (int neighbor : graph[i]) {
                    inDegree[neighbor]--;
                }
                // Recurse with updated state
                maxProfit = Math.max(maxProfit, backtrack(currentOrder, visited, inDegree, graph, score));
                // Backtrack - undo choices
                for (int neighbor : graph[i]) {
                    inDegree[neighbor]++;
                }
                currentOrder.remove(currentOrder.size() - 1);
                visited[i] = false;
            }
        }
        return maxProfit;
    }

    private int calculateProfit(List<Integer> order, int[] score) {								 					 	 	 	 	 	 	 	 	 	 			 	    int profit = 0;	    for (int i = 0; i < order.size(); i++) {          profit += score[order.get(i)] * (i + 1);      }      return profit;   }   } # @lc code=end