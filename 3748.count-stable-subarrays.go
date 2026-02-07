#
# @lc app=leetcode id=3748 lang=golang
#
# [3748] Count Stable Subarrays
#

# @lc code=start
func countStableSubarrays(nums []int, queries [][]int) []int64 {
    n := len(nums)
    nextBreak := make([]int, n) // nextBreak[i] is the last index of the non-decreasing run starting at i
    nextBreak[n-1] = n-1
    for i := n-2; i >= 0; i-- {
        if nums[i] <= nums[i+1] {
            nextBreak[i] = nextBreak[i+1]
        } else {
            nextBreak[i] = i
        }
    }
    ans := make([]int64, len(queries))
    for qi, q := range queries {
        l, r := q[0], q[1]
        res := int64(0)
        i := l
        for i <= r {
            j := nextBreak[i]
            if j > r {
                j = r
            }
            lenRun := j - i + 1
            res += int64(lenRun) * int64(lenRun+1) / 2
            i = j + 1
        }
        ans[qi] = res
    }
    return ans
}
# @lc code=end