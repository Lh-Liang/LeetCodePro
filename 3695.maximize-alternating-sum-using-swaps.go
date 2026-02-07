#
# @lc app=leetcode id=3695 lang=golang
#
# [3695] Maximize Alternating Sum Using Swaps
#

# @lc code=start
import (
    "sort"
)

func maxAlternatingSum(nums []int, swaps [][]int) int64 {
    n := len(nums)
    parent := make([]int, n)
    for i := range parent {
        parent[i] = i
    }
    var find func(int) int
    find = func(x int) int {
        if parent[x] != x {
            parent[x] = find(parent[x])
        }
        return parent[x]
    }
    union := func(x, y int) {
        px, py := find(x), find(y)
        if px != py {
            parent[py] = px
        }
    }
    for _, swap := range swaps {
        union(swap[0], swap[1])
    }
    groups := make(map[int][]int)
    for i := 0; i < n; i++ {
        root := find(i)
        groups[root] = append(groups[root], i)
    }
    res := int64(0)
    for _, idxs := range groups {
        values := make([]int, len(idxs))
        for i, idx := range idxs {
            values[i] = nums[idx]
        }
        sort.Ints(idxs)
        sort.Sort(sort.Reverse(sort.IntSlice(values)))
        evenIdxs, oddIdxs := []int{}, []int{}
        for _, idx := range idxs {
            if idx%2 == 0 {
                evenIdxs = append(evenIdxs, idx)
            } else {
                oddIdxs = append(oddIdxs, idx)
            }
        }
        // Assign largest values to even indices, smallest to odd
        evenCount := len(evenIdxs)
        oddCount := len(oddIdxs)
        sum := int64(0)
        for i := 0; i < evenCount; i++ {
            sum += int64(values[i])
        }
        for i := 0; i < oddCount; i++ {
            sum -= int64(values[evenCount+i])
        }
        res += sum
    }
    return res
}
# @lc code=end