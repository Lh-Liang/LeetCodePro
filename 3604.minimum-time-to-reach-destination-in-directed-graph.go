#
# @lc app=leetcode id=3604 lang=golang
#
# [3604] Minimum Time to Reach Destination in Directed Graph
#

# @lc code=start
package main

import (
    "container/heap"
    "math"
)

type Edge struct {
    target, start, end int
}

type State struct {
    node, time int
}
type PriorityQueue []State
func (pq PriorityQueue) Len() int { return len(pq) }
func (pq PriorityQueue) Less(i, j int) bool { return pq[i].time < pq[j].time }
func (pq PriorityQueue) Swap(i, j int) { pq[i], pq[j] = pq[j], pq[i] }
func (pq *PriorityQueue) Push(x interface{}) { *pq = append(*pq, x.(State)) }
func (pq *PriorityQueue) Pop() interface{} { old := *pq; n := len(old); item := old[n-1]; *pq = old[0 : n-1]; return item } 
type Graph map[int][]Edge 
func minTime(n int, edges [][]int) int { 
graph := make(Graph) 
for _, edge := range edges { 
graph[edge[0]] = append(graph[edge[0]], Edge{edge[1], edge[2], edge[3]}) 
} 
dist := make([]int, n) 
for i := range dist { dist[i] = math.MaxInt64 } 
dist[0] = 0 
pq := &PriorityQueue{{0, 0}} 
heap.Init(pq) 
for pq.Len() > 0 { state := heap.Pop(pq).(State) if state.node == n-1 { return state.time } if state.time > dist[state.node] { continue } for _, edge := range graph[state.node] { nextTime := max(state.time+1, edge.start) if nextTime <= edge.end && nextTime < dist[edge.target] { dist[edge.target] = nextTime heap.Push(pq, State{edge.target, nextTime}) }} } return -1 } func max(a, b int) int { if a > b { return a } else { return b }} # @lc code=end