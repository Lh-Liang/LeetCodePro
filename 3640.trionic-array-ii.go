#
# @lc app=leetcode id=3640 lang=golang
#
# [3640] Trionic Array II
#

# @lc code=start
func maxSumTrionic(nums []int) int64 {
    n := len(nums)
    prefix := make([]int64, n+1)
    for i := 0; i < n; i++ {
        prefix[i+1] = prefix[i] + int64(nums[i])
    }
    // Precompute length of strictly increasing sequences ending at i
    incLeft := make([]int, n)
    for i := 1; i < n; i++ {
        if nums[i-1] < nums[i] {
            incLeft[i] = incLeft[i-1] + 1
        } else {
            incLeft[i] = 0
        }
    }
    // Precompute length of strictly increasing sequences starting at i
    incRight := make([]int, n)
    for i := n-2; i >= 0; i-- {
        if nums[i] < nums[i+1] {
            incRight[i] = incRight[i+1] + 1
        } else {
            incRight[i] = 0
        }
    }
    // Precompute length of strictly decreasing sequences ending at i
    decLeft := make([]int, n)
    for i := 1; i < n; i++ {
        if nums[i-1] > nums[i] {
            decLeft[i] = decLeft[i-1] + 1
        } else {
            decLeft[i] = 0
        }
    }
    // Precompute length of strictly decreasing sequences starting at i
    decRight := make([]int, n)
    for i := n-2; i >= 0; i-- {
        if nums[i] > nums[i+1] {
            decRight[i] = decRight[i+1] + 1
        } else {
            decRight[i] = 0
        }
    }
    maxSum := int64(-1<<63)
    // For each possible middle (peak of decreasing segment), try all possible q (end of decreasing, start of last increasing)
    for q := 2; q < n-1; q++ {
        // q is the end of decreasing, the strictly decreasing segment is from p to q
        decLen := decLeft[q]
        if decLen == 0 {
            continue
        }
        p := q - decLen
        // The first strictly increasing segment ends at p, so it starts at l = p - incLeft[p]
        inc1Len := incLeft[p]
        l := p - inc1Len
        if l >= 0 && l < p && p < q {
            // The last strictly increasing segment starts at q, so it ends at r = q + incRight[q]
            inc2Len := incRight[q]
            r := q + inc2Len
            if r < n && q < r {
                sum := prefix[r+1] - prefix[l]
                if sum > maxSum {
                    maxSum = sum
                }
            }
        }
    }
    return maxSum
}
# @lc code=end