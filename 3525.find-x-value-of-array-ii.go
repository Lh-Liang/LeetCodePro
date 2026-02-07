#
# @lc app=leetcode id=3525 lang=golang
#
# [3525] Find X Value of Array II
#

# @lc code=start
func resultArray(nums []int, k int, queries [][]int) []int {
    n := len(nums)
    res := make([]int, len(queries))
    curr := make([]int, n)
    copy(curr, nums)
    for qi, q := range queries {
        idx, val, start, x := q[0], q[1], q[2], q[3]
        curr[idx] = val
        arr := curr[start:]
        m := len(arr)
        prefixProd := make([]int, m+1)
        prefixProd[0] = 1
        for i := 0; i < m; i++ {
            prefixProd[i+1] = (prefixProd[i] * arr[i]) % k
        }
        count := 0
        for j := 1; j <= m; j++ {
            if prefixProd[j] == x {
                count++
            }
        }
        res[qi] = count
    }
    return res
}
# @lc code=end