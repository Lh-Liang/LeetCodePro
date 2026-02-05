# @lc app=leetcode id=3585 lang=java
#
# [3585] Find Weighted Median Node in Tree
#
# @lc code=start
import java.util.*;

class Solution {
    public int[] findMedian(int n, int[][] edges, int[][] queries) {
        Map<Integer, List<int[]>> tree = new HashMap<>();
        for (int[] edge : edges) {
            tree.computeIfAbsent(edge[0], k -> new ArrayList<>()).add(new int[]{edge[1], edge[2]});
            tree.computeIfAbsent(edge[1], k -> new ArrayList<>()).add(new int[]{edge[0], edge[2]});
        }
        
        // Initialize data structures for storing parent, depth, and cumulative weights
        int[] parent = new int[n];
        int[] depth = new int[n];
        long[] cumWeight = new long[n];
        Arrays.fill(parent, -1);

        // Preprocess with DFS to compute parents and cumulative weights
        dfs(tree, 0, -1, 0L, 0, parent, depth, cumWeight);

        // Determine LCA using binary lifting or sparse table methods (not detailed here)
        // This is a placeholder where LCA preprocessing would occur.
        
        int[] result = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int uj = queries[i][0];
            int vj = queries[i][1];
            
            // Determine path using LCA and calculate total path weight.
            long totalPathWeight = findPathWeight(uj, vj, parent, cumWeight);
            long halfWeight = totalPathWeight / 2;
            
            // Traverse path to find weighted median node based on cumulative weights.
            result[i] = findMedianNode(uj, vj, halfWeight, parent, cumWeight);
        }
        return result;
    }

    private void dfs(Map<Integer, List<int[]>> tree, int node, int par, long weightSum,
t depthSum,
t[] parent,
t[] depth,
t[] cumWeight) {
t     parent[node] = par;
t     depth[node] = depthSum;
t     cumWeight[node] = weightSum;
t     for (int[] neighbor : tree.getOrDefault(node,k new ArrayList<>())) {
t         if (neighbor[0] != par) {
t             dfs(tree,k neighbor[0],k node,k weightSum + neighbor[1],k depthSum + 1,k parent,k depth,k cumWeight);
t         }		}	}		public long findPathWeight(int uj,int vj,int[] parent,long[] cumWeight) {		// Calculate total path weight from uj to vj using LCA logic		// This is a placeholder function that requires actual LCA logic implementation		return Math.abs(cumWeight[uj] - cumWeight[vj]);	}	public int findMedianNode(int uj,int vj,long halfWeight,int[] parent,long[] cumWeight) {		// Traverse nodes from uj/vj towards their LCA,		// summing weights until reaching/exceeding half of total path weight,		// return corresponding median node index.		// Placeholder logic that should be replaced with actual traversal implementation.		return -1;	}	} # @lc code=end