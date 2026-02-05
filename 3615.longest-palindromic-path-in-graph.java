# @lc app=leetcode id=3615 lang=java
#
# [3615] Longest Palindromic Path in Graph
#
# @lc code=start
import java.util.*;

class Solution {
    public int maxLen(int n, int[][] edges, String label) {
        // Step 1: Create adjacency list for the graph
        List<Integer>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int[] edge : edges) {
            graph[edge[0]].add(edge[1]);
            graph[edge[1]].add(edge[0]);
        }

        int maxLength = 0;
        int totalMasks = 1 << n; // Total number of subsets represented by bitmasks

        // Step 2-6: Iterate through all subsets using bitmasks and check for palindromic paths
        for (int mask = 1; mask < totalMasks; mask++) {
            if (isConnected(mask, graph)) {
                maxLength = Math.max(maxLength, maxPalindromeLength(mask, label));
            }
        }

        return maxLength;
    }

    private boolean isConnected(int mask, List<Integer>[] graph) {
        // Check if nodes represented by 'mask' form a connected component in the graph
        int startNode = Integer.numberOfTrailingZeros(mask); // Find first node in mask to start DFS from
        Queue<Integer> queue = new LinkedList<>();
        boolean[] visited = new boolean[graph.length];
        queue.add(startNode);
        visited[startNode] = true;

        int count = 0;
        while (!queue.isEmpty()) {
            int node = queue.poll();
            count++;
            for (int neighbor : graph[node]) {
                if (!visited[neighbor] && ((mask & (1 << neighbor)) != 0)) {
                    visited[neighbor] = true;
                    queue.add(neighbor);
                }
            }
        }

        return count == Integer.bitCount(mask); // Check if all nodes in 'mask' are visited
    }

    private int maxPalindromeLength(int mask, String label) {			// Calculate max palindrome length from nodes in 'mask'			int[] charCount = new int[26]; // Count characters			for (int i = 0; i < label.length(); i++) {				if ((mask & (1 << i)) != 0) { // If node i is in the current subset					charCount[label.charAt(i) - 'a']++;				}			}			int oddCount = 0;			for (int count : charCount) {				if (count % 2 != 0) oddCount++;	}	return oddCount <= 1 ? Integer.bitCount(mask) : Integer.bitCount(mask) - oddCount + 1; // Max possible palindrome length}	}// @lc code=end