#
# @lc app=leetcode id=3762 lang=golang
#
# [3762] Minimum Operations to Equalize Subarrays
#

# @lc code=start
func minOperations(nums []int, k int, queries [][]int) []int64 {
    ans := make([]int64, len(queries))
    
    for i, query := range queries {
        li, ri := query[0], query[1]
        subarray := nums[li:ri+1]
        ops := calculateMinOperations(subarray, k)
        ans[i] = ops
    }
    
    return ans
}

func calculateMinOperations(subarray []int, k int) int64 {
    n := len(subarray)
    if n == 1 {
        return 0 // Already equal
    }
    
    // Check feasibility of making all elements equal and calculate minimal operations
    ops := int64(-1)
    for targetIndex := range subarray {
        currentOps := int64(0)
        feasible := true
        target := subarray[targetIndex]
        for _, num := range subarray {
            diff := abs(num - target)
            if diff % k != 0 {
                feasible = false
                break
            }
            currentOps += int64(diff / k)
        }
        if feasible && (ops == -1 || currentOps < ops) {
            ops = currentOps
        }
    }
    return ops
}

func abs(a int) int {
    if a < 0 {
        return -a
    }
    return a
}
# @lc code=end