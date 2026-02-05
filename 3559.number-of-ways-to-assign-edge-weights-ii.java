#
# @lc app=leetcode id=3559 lang=java
#
# [3559] Number of Ways to Assign Edge Weights II
#
# @lc code=start
import java.util.*;

class Solution {
    private static final int MOD = 1000000007;
    private List<Integer>[] tree;
    private int[] parent;
    private int[] depth;
    
    public int[] assignEdgeWeights(int[][] edges, int[][] queries) {
        int n = edges.length + 1;
        tree = new ArrayList[n + 1];
        parent = new int[n + 1];
        depth = new int[n + 1];
        Arrays.fill(parent, -1);
        
        for (int i = 0; i <= n; i++) {
            tree[i] = new ArrayList<>();
        }
        
        for (int[] edge : edges) {
            int u = edge[0], v = edge[1];
            tree[u].add(v);
            tree[v].add(u);
        }
        
        dfs(1, -1, 0);
        
        int[] answer = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int u = queries[i][0], v = queries[i][1];
            answer[i] = countOddPaths(u, v);
        }
        return answer;
    }
    
    private void dfs(int node, int par, int d) {
        parent[node] = par;
        depth[node] = d;
        for (int neighbor : tree[node]) {
            if (neighbor != par) {
                dfs(neighbor, node, d + 1);
            }
        }
    }

    private int lca(int u, int v) {	
	while(depth[u] > depth[v]) u=parent[u];	while(depth[v] > depth[u]) v=parent[v];	while(u != v){	u=parent[u];v=parent[v];}	return u;}	private long combination(int n,int r){ 	long result=1L;for(int i=0;i<r;i++){result=result*(long)(nt-i)/(long)(i+1)%MOD;}return result;}private int countOddPaths(int u,int v){int lcaNode=lca(u,v);int pathLength=depth[u]+depth[v]-2*depth[lcaNode];int ways=0;for(int i=1;i<=pathLength;i+=2){ways=(ways+combination(pathLength,i))%MOD;}return ways;}