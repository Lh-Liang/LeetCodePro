import "container/heap"
import "math"

type Edge struct {
    to    int
    start int
    end   int
}
type Item struct {
    node int
    time int64
}
type PriorityQueue []*Item
func (pq PriorityQueue) Len() int { return len(pq) }
func (pq PriorityQueue) Less(i, j int) bool { return pq[i].time < pq[j].time }
func (pq PriorityQueue) Swap(i, j int) { pq[i], pq[j] = pq[j], pq[i] }
func (pq *PriorityQueue) Push(x interface{}) { *pq = append(*pq, x.(*Item)) }
func (pq *PriorityQueue) Pop() interface{} {
    old := *pq
    n := len(old)
    item := old[n-1]
    *pq = old[0 : n-1]
    return item
}
func minTime(n int, edges [][]int) int {
    graph := make([][]Edge, n)
    for _, edge := range edges {
        u, v, start, end := edge[0], edge[1], edge[2], edge[3]
        graph[u] = append(graph[u], Edge{v, start, end})
    }

    pq := &PriorityQueue{}
    heap.Init(pq)
    heap.Push(pq, &Item{node: 0, time: 0})

    dist := make([]int64, n)
    for i := range dist {
        dist[i] = math.MaxInt64 // infinity
    }
    dist[0] = 0

    for pq.Len() > 0 {
        item := heap.Pop(pq).(*Item)
        if item.time > dist[item.node] {
            continue
        }
        for _, e := range graph[item.node] {
            waitTime := max(item.time, e.start)
            if waitTime <= e.end && waitTime+1 < dist[e.to] {
                dist[e.to] = waitTime + 1
                heap.Push(pq, &Item{node: e.to, time: dist[e.to]})
            }
        }
    }

    if dist[n-1] == math.MaxInt64 {
        return -1
    }
    return int(dist[n-1])
}
type PriorityQueue []*Item