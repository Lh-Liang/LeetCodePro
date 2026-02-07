#
# @lc app=leetcode id=3762 lang=golang
#
# [3762] Minimum Operations to Equalize Subarrays
#

# @lc code=start
import (
    "sort"
)

func minOperations(nums []int, k int, queries [][]int) []int64 {
    n := len(nums)
    res := make([]int64, len(queries))
    for qi, q := range queries {
        l, r := q[0], q[1]
        m := r - l + 1
        mods := nums[l : r+1]
        mod0 := mods[0] % k
        feasible := true
        vals := make([]int, m)
        for i := 0; i < m; i++ {
            if mods[i]%k != mod0 {
                feasible = false
                break
            }
            vals[i] = (mods[i] - mod0) / k
        }
        if !feasible {
            res[qi] = -1
            continue
        }
        if m == 1 {
            res[qi] = 0
            continue
        }
        sort.Ints(vals)
        median := vals[m/2]
        var ops int64 = 0
        for i := 0; i < m; i++ {
            ops += int64(abs(vals[i] - median))
        }
        res[qi] = ops
    }
    return res
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}
# @lc code=end