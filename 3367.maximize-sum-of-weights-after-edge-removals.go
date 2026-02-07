# @lc app=leetcode id=3367 lang=golang
#
# [3367] Maximize Sum of Weights after Edge Removals
#
# @lc code=start
package main

import "sort"

func maximizeSumOfWeights(edges [][]int, k int) int64 {
    n := len(edges) + 1 // Number of nodes
    totalWeight := int64(0)
    
    // Initialize adjacency list and weight tracking
    adjList := make([][]int, n)
    weights := make(map[[2]int]int)
    
    for _, edge := range edges {
        u, v, w := edge[0], edge[1], edge[2]
        adjList[u] = append(adjList[u], v)
        adjList[v] = append(adjList[v], u)
        weights[[2]int{u,v}] = w
        weights[[2]int{v,u}] = w // undirected graph representation
        totalWeight += int64(w)
    }
    
    // Sort edges by weight descending order for consideration in removal strategy
    sort.Slice(edges, func(i, j int) bool {
        return edges[i][2] > edges[j][2]
    })
    
    // Union-Find data structure to track connectivity
    parent := make([]int, n)
    rank := make([]int, n)
    for i := range parent {
        parent[i] = i
        rank[i] = 1
    }

    var find func(int) int
    find = func(x int) int {
        if parent[x] != x {
            parent[x] = find(parent[x])
        }
        return parent[x]
    }

    union := func(x, y int) bool {
        rootX := find(x)
        rootY := find(y)
        if rootX != rootY {
            if rank[rootX] > rank[rootY] {
                parent[rootY] = rootX
            } else if rank[rootX] < rank[rootY] {
                parent[rootX] = rootY
            } else {
                parent[rootY] = rootX
                rank[rootX]++
            }
            return true // successfully united different components
        }
        return false // already in the same component  not needed for removal verification but ensures connectivity check later on }// Attempt to reduce connections while maintaining tree integrityfunc canRemoveEdge(u,v int) bool { return find(u)!=find(v)}for _, edge:=range edges {u,v,w:=edge[0],edge[1],edge[2]ifadjList[u]>k||adjList[v]>k {ifcanRemoveEdge(u,v){adjList[u]=remove(adjList[u],v)
adjList[v]=remove(adjList[v],u)
totalWeight-=int64(w)}}}eturn totalWeight}unc remove(slice []int,val int ) []int {for i,n:=range slice {if n==val{slice[i]=slice[len(slice)-1]
slice=slice[:len(slice)-1]
break}}eturn slice}/lc code=end