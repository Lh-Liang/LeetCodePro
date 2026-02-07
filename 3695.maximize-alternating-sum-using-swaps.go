#
# @lc app=leetcode id=3695 lang=golang
#
# [3695] Maximize Alternating Sum Using Swaps
#

# @lc code=start
func maxAlternatingSum(nums []int, swaps [][]int) int64 {
    n := len(nums)
    parent := make([]int, n)
    for i := range parent {
        parent[i] = i
    }
    var find func(x int) int
    find = func(x int) int {
        if parent[x] != x {
            parent[x] = find(parent[x])
        }
        return parent[x]
    }
    union := func(x, y int) {
        rootX := find(x)
        rootY := find(y)
        if rootX != rootY {
            parent[rootX] = rootY
        }
    }
    for _, swap := range swaps {
        union(swap[0], swap[1])
    }
    components := make(map[int][]int)
    for i := 0; i < n; i++ {
        root := find(i)
        components[root] = append(components[root], nums[i])
    }
    result := int64(0)
    for _, comp := range components {
        sort.Slice(comp, func(i, j int) bool { return comp[i] > comp[j] }) // Sort in descending order to maximize alternating sum.
       for i, num := range comp { 
           if i%2 == 0 { 
               result += int64(num) 
           } else { 
               result -= int64(num) 
           } 
       } 
   } 
   return result 
} # @lc code=end