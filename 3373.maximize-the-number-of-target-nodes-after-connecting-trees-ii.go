#
# @lc app=leetcode id=3373 lang=golang
#
# [3373] Maximize the Number of Target Nodes After Connecting Trees II
#

# @lc code=start
package main

import (
    "container/list"
)

func maxTargetNodes(edges1 [][]int, edges2 [][]int) []int {
    n := len(edges1) + 1
    m := len(edges2) + 1
    
    // Build adjacency lists for both trees
    adjList1 := make([][]int, n)
    adjList2 := make([][]int, m)
    for _, edge := range edges1 {
        u, v := edge[0], edge[1]
        adjList1[u] = append(adjList1[u], v)
        adjList1[v] = append(adjList1[v], u)
    }
    
    for _, edge := range edges2 {
        u, v := edge[0], edge[1]
        adjList2[u] = append(adjList2[u], v)
        adjList2[v] = append(adjList2[v], u)
    }

    // BFS to determine distance from each node to all others in Tree 2
    bfsDistances := func(start int, adjList [][]int) []int {
        distances := make([]int, len(adjList))
        for i := range distances {
            distances[i] = -1 // unvisited marker
        }
        queue := list.New()
        queue.PushBack(start)
        distances[start] = 0
        
        for queue.Len() > 0 {
            current := queue.Remove(queue.Front()).(int)
            currentDistance := distances[current]
            
            for _, neighbor := range adjList[current] {
                if distances[neighbor] == -1 { // not visited yet
                    distances[neighbor] = currentDistance + 1
                    queue.PushBack(neighbor)
                }
            }
        }
        return distances
    }
    
    // Precompute distances from all nodes in Tree 2 to every other node using LCA or similar efficient methods.
    distMatrixTree2 := make([][]int, m)
    for i := 0; i < m; i++ {
        distMatrixTree2[i] = bfsDistances(i, adjList2)
    }
    
    result := make([]int, n)

    // Calculate maximum targetable nodes for each node in Tree 1 by connecting Tree 2 optimally using efficient traversal techniques.

    for i := 0; i < n; i++ { 
        maxTargets := 0

        // Try connecting every node j from Tree 2 and calculate how many are targets efficiently.

        for j := 0; j < m; j++ { 
            targetsCount := 0
            	// Implement optimized check leveraging precomputed data like LCA results if available.	for _, dist := range distMatrixTree2[j] { 	if dist % 2 == 0 && dist != -1 { // -1 means unreachable so should not count that	targetsCount++	} 	} 	if targetsCount > maxTargets { 	maxTargets = targetsCount	} 	} 	result[i] = maxTargets	} return result }