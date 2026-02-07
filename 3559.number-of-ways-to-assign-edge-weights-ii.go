#
# @lc app=leetcode id=3559 lang=golang
#
# [3559] Number of Ways to Assign Edge Weights II
#

# @lc code=start
func assignEdgeWeights(edges [][]int, queries [][]int) []int {
    // Initialize necessary structures: adjacency list and results array
    n := len(edges) + 1 // Number of nodes
    adjList := make([][]int, n+1)
    mod := int(1e9 + 7)
    results := make([]int, len(queries))
    
    // Build adjacency list from edges
    for _, edge := range edges {
        u, v := edge[0], edge[1]
        adjList[u] = append(adjList[u], v)
        adjList[v] = append(adjList[v], u)
    }
    
    // Preprocess paths using DFS to find parents and depths
    parent := make([]int, n+1)
    depth := make([]int, n+1)
    var dfs func(node, par int)
    dfs = func(node, par int) {
        parent[node] = par
        for _, neighbor := range adjList[node] {
            if neighbor != par {
                depth[neighbor] = depth[node] + 1
                dfs(neighbor, node)
            }
        }
    }
    dfs(1, -1) // Assume root at node 1
    
    // Function to find LCA (Lowest Common Ancestor), used for finding paths
    findLCA := func(u, v int) int {if depth[u] < depth[v] {u, v = v, u}for depth[u] > depth[v] {u = parent[u]}for u != v {u = parent[u]
v = parent[v]}return u}// Calculate number of valid ways for each query
for i, query:= range queries{
distances=0 // Reset distance counts 
totalEdges:=0 
u,v:=query[0],query[1]
lca:=findLCA(u,v) // Find LCA 
fpath:={make(map[int]int)}// Track frequencies along path 
fpath[u]+=fpath[v]+=fpath[lca]-=2*fpath[parent[lca]]// Adjust frequencies 
totalEdges=depth[u]+depth[v]-2*depth[lca]
distances=(totalEdges+distances)%mod// Update distances modulo 
vways:=(distances-((totalEdges-distances)/2))%mod// Calculate valid ways 
nways:=(distances/2)%mod// Calculate new ways 
vways+=modulo(vways)// Add modulo constraint 
nways+=modulo(nways)// Add modulo constraint 
vways%=mod// Apply final modulo constraint 
nways%=mod// Apply final modulo constraint }// End loop over queries return results }// Return final result # @lc code=end