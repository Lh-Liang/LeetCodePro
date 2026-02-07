#
# @lc app=leetcode id=3604 lang=golang
#
# [3604] Minimum Time to Reach Destination in Directed Graph
#

# @lc code=start
import (
    "container/heap"
    "math"
)

type Edge struct {
    to, start, end int
}

type Item struct {
    time, node int
}

type PriorityQueue []Item

func (pq PriorityQueue) Len() int { return len(pq) }
func (pq PriorityQueue) Less(i, j int) bool { return pq[i].time < pq[j].time }
func (pq PriorityQueue) Swap(i, j int) { pq[i], pq[j] = pq[j], pq[i] }
func (pq *PriorityQueue) Push(x interface{}) { *pq = append(*pq, x.(Item)) }
func (pq *PriorityQueue) Pop() interface{} {
    old := *pq
    n := len(old)
    x := old[n-1]
    *pq = old[0 : n-1]
    return x
}

func minTime(n int, edges [][]int) int {
    // Build adjacency list
    graph := make([][]Edge, n)
    for _, e := range edges {
        u, v, s, e2 := e[0], e[1], e[2], e[3]
        graph[u] = append(graph[u], Edge{to: v, start: s, end: e2})
    }
    // Dijkstra's / BFS with time
    pq := &PriorityQueue{}
    heap.Init(pq)
    heap.Push(pq, Item{time: 0, node: 0})
    visited := make([]int, n)
    for i := range visited {
        visited[i] = math.MaxInt64
    }
    visited[0] = 0
    for pq.Len() > 0 {
        it := heap.Pop(pq).(Item)
        t, u := it.time, it.node
        if u == n-1 {
            return t
        }
        if t > visited[u] {
            continue
        }
        for _, e := range graph[u] {
            // Wait until the edge can be used
            if t > e.end {
                continue
            }
            depart := t
            if depart < e.start {
                depart = e.start
            }
            if depart > e.end {
                continue
            }
            arrive := depart + 1
            if arrive < visited[e.to] {
                visited[e.to] = arrive
                heap.Push(pq, Item{time: arrive, node: e.to})
            }
        }
    }
    return -1
}
# @lc code=end