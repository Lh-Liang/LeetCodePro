#
# @lc app=leetcode id=3768 lang=golang
#
# [3768] Minimum Inversion Count in Subarrays of Fixed Length
#

# @lc code=start
func minInversionCount(nums []int, k int) int64 {
    n := len(nums)
    minInversions := int64(n * n) // Initialize with a large number
    for i := 0; i <= n-k; i++ {
        _, count := mergeSortAndCount(nums[i:i+k])
        if count < minInversions {
            minInversions = count
        }
    }
    return minInversions
}

func mergeSortAndCount(arr []int) ([]int, int64) {
    if len(arr) < 2 {
        return arr, 0
    }
    mid := len(arr) / 2
    left, leftInv := mergeSortAndCount(arr[:mid])
    right, rightInv := mergeSortAndCount(arr[mid:])
    mergedArr, splitInv := mergeAndCount(left, right)
    return mergedArr, leftInv + rightInv + splitInv
}

func mergeAndCount(left []int, right []int) ([]int, int64) {
    i, j := 0, 0
    var invCount int64 = 0
    mergedArr := make([]int, 0, len(left)+len(right))
    for i < len(left) && j < len(right) {
        if left[i] <= right[j] {
            mergedArr = append(mergedArr, left[i])
            i++
        } else { // there are mid - i inversions because left[i] > right[j]
            mergedArr = append(mergedArr, right[j])
            invCount += int64(len(left) - i) & // Count inversions here & j++ & } & } & & // Append remaining elements & mergedArr = append(mergedArr,left[i:]...) & mergedArr = append(mergedArr,right[j:]...) & return mergedArr , invCount & } # @lc code=end