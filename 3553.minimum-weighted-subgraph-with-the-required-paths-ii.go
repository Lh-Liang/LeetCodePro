# @lc app=leetcode id=3553 lang=golang
# [3553] Minimum Weighted Subgraph With the Required Paths II
#
# @lc code=start
import "container/heap"

type Item struct {
    node int
    distance int
}
type PriorityQueue []*Item
func (pq PriorityQueue) Len() int { return len(pq) }
func (pq PriorityQueue) Less(i, j int) bool { return pq[i].distance < pq[j].distance }
func (pq PriorityQueue) Swap(i, j int) { pq[i], pq[j] = pq[j], pq[i] }
func (pq *PriorityQueue) Push(x interface{}) { *pq = append(*pq, x.(*Item)) }
func (pq *PriorityQueue) Pop() interface{} {
    old := *pq
    n := len(old)
    item := old[n-1]
    *pq = old[0 : n-1]
    return item
}

func dijkstra(n int, adjList [][]struct{node, weight int}, start int) []int {
    dist := make([]int, n)
    for i := range dist {
        dist[i] = 1<<63 - 1 // MaxInt equivalent in Go for infinity representation
    }
    dist[start] = 0
    pq := &PriorityQueue{{start, 0}}
    heap.Init(pq)
    
    for pq.Len() > 0 {
        current := heap.Pop(pq).(*Item)
        u := current.node
        if current.distance > dist[u] {
            continue // Skip if a shorter path has been found already
        }
        for _, neighbor := range adjList[u] {
            v, w := neighbor.node, neighbor.weight
            newDist := dist[u] + w
            if newDist < dist[v] {
                dist[v] = newDist
                heap.Push(pq, &Item{v, newDist})
            }
        }
    }
    return dist
}

func minimumWeight(edges [][]int, queries [][]int) []int {
    n := len(edges) + 1
    adjList := make([][]struct{node, weight int}, n)
   
    // Build adjacency list from edges input
    for _, edge := range edges {
        u, v, w := edge[0], edge[1], edge[2]
        adjList[u] = append(adjList[u], struct{node, weight int}{v, w})
        adjList[v] = append(adjList[v], struct{node, weight int}{u, w})
    }
   
   result := make([]int, len(queries))
   	for i, q := range queries {
src1, src2 , dest:= q[0], q[1], q[2]
distFromSrc1:= dijkstra(n ,adjList ,src1 )
distFromSrc2:= dijkstra(n ,adjList ,src2 )
distToDest:= dijkstra(n ,adjList ,dest )		minWeightSubtree:= 1<<63 -1// MaxInt equivalent initially		for v:=0; v<n ; v++{		if distFromSrc1[v]!=1<<63-1 &&distFromSrc2[v]!=1<<63-1 &&distToDest[v]!=1<<63-1{	totalWeight:=distFromSrc1[v]+distFromSrc2[v]+distToDest[v]	if totalWeight<minWeightSubtree{	minWeightSubtree=totalWeight	}	}	}	result[i]=minWeightSubtree	}	return result	}