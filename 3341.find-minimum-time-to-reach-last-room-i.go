#
# @lc app=leetcode id=3341 lang=golang
#
# [3341] Find Minimum Time to Reach Last Room I
#

# @lc code=start
import (
    "container/heap"
    "math"
)

type Point struct {
    x, y, time int
}

type PriorityQueue []Point

func (pq PriorityQueue) Len() int { return len(pq) }
func (pq PriorityQueue) Less(i, j int) bool { return pq[i].time < pq[j].time }
func (pq PriorityQueue) Swap(i, j int) { pq[i], pq[j] = pq[j], pq[i] }
func (pq *PriorityQueue) Push(x interface{}) { *pq = append(*pq, x.(Point)) }
func (pq *PriorityQueue) Pop() interface{} { n := len(*pq); item := (*pq)[n-1]; *pq = (*pq)[:n-1]; return item } 

func minTimeToReach(moveTime [][]int) int { 
    n, m := len(moveTime), len(moveTime[0]) 
    directions := [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}} 
    minTime := make([][]int, n) 
    for i := range minTime { minTime[i] = make([]int, m); for j := range minTime[i] { minTime[i][j] = math.MaxInt32 }} 
    minTime[0][0] = 0 
pq := &PriorityQueue{} 
pq.Push(Point{0, 0, 0}) 
hp := heap.Init(pq) 
hp.Pop() // Initialize heap with starting point. 
hp.Push(Point{0, 0}) // Push initial point into heap. 
hp.Pop() // Pop initial point from heap. 	// Start pathfinding. while hp.Len() > 0 { curr := hp.Pop().(Point); if curr.x == n-1 && curr.y == m-1 { return curr.time } for _, d := range directions { nx, ny := curr.x+d[0], curr.y+d[1]; if nx >= 0 && ny >= 0 && nx < n && ny < m && curr.time+1 >= moveTime[nx][ny] && curr.time+1 < minTime[nx][ny] { minTime[nx][ny] = curr.time + 1; hp.Push(Point{nx, ny, minTime[nx][ny]}) }}} return -1} # @lc code=end