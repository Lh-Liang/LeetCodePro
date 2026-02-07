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

type Item struct {
    time, x, y int
}

type PriorityQueue []Item

func (pq PriorityQueue) Len() int { return len(pq) }
func (pq PriorityQueue) Less(i, j int) bool { return pq[i].time < pq[j].time }
func (pq PriorityQueue) Swap(i, j int) { pq[i], pq[j] = pq[j], pq[i] }
func (pq *PriorityQueue) Push(x interface{}) {
    *pq = append(*pq, x.(Item))
}
func (pq *PriorityQueue) Pop() interface{} {
    old := *pq
    n := len(old)
    item := old[n-1]
    *pq = old[:n-1]
    return item
}

func minTimeToReach(moveTime [][]int) int {
    n, m := len(moveTime), len(moveTime[0])
    dirs := [][]int{{0,1},{1,0},{0,-1},{-1,0}}
    dist := make([][]int, n)
    for i := 0; i < n; i++ {
        dist[i] = make([]int, m)
        for j := 0; j < m; j++ {
            dist[i][j] = math.MaxInt32
        }
    }
    dist[0][0] = 0
    pq := &PriorityQueue{}
    heap.Init(pq)
    heap.Push(pq, Item{0, 0, 0})
    for pq.Len() > 0 {
        it := heap.Pop(pq).(Item)
        t, x, y := it.time, it.x, it.y
        if x == n-1 && y == m-1 {
            return t
        }
        if t > dist[x][y] {
            continue
        }
        for _, d := range dirs {
            nx, ny := x + d[0], y + d[1]
            if nx >= 0 && nx < n && ny >= 0 && ny < m {
                arrive := max(t+1, moveTime[nx][ny])
                if arrive < dist[nx][ny] {
                    dist[nx][ny] = arrive
                    heap.Push(pq, Item{arrive, nx, ny})
                }
            }
        }
    }
    return -1
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
# @lc code=end