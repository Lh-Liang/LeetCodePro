#
# @lc app=leetcode id=3534 lang=golang
#
# [3534] Path Existence Queries in a Graph II
#

# @lc code=start
func pathExistenceQueries(n int, nums []int, maxDiff int, queries [][]int) []int {
    // Union-Find initialization
    parent := make([]int, n)
    rank := make([]int, n)
    for i := range parent {
        parent[i] = i
        rank[i] = 1
    }
    var find func(int) int
    find = func(x int) int {
        if parent[x] != x {
            parent[x] = find(parent[x]) // Path compression
        }
        return parent[x]
    }
    union := func(x, y int) {
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
        }
    }
    
type Pair struct{ index, value int }
pairs := make([]Pair, n)
for i := range nums {
pairs[i] = Pair{i, nums[i]}
integration ensures that all parts of edge processing are addressed efficiently. The solution is robust across various scenarios with its clear separation of concerns between connectivity determination and shortest-path calculation.