#
# @lc app=leetcode id=3721 lang=golang
#
# [3721] Longest Balanced Subarray II
#
# @lc code=start
func longestBalanced(nums []int) int {
    evenMap := make(map[int]int)
    oddMap := make(map[int]int)
    left := 0
    maxLen := 0
    for right, num := range nums {
        if num%2 == 0 {
            evenMap[num]++
        } else {
            oddMap[num]++
        }
        for left <= right && len(evenMap) > len(oddMap) {
            if nums[left]%2 == 0 {
                evenMap[nums[left]]--
                if evenMap[nums[left]] == 0 {
                    delete(evenMap, nums[left])
                }
            } else {
                oddMap[nums[left]]--
                if oddMap[nums[left]] == 0 {
                    delete(oddMap, nums[left])
                }
            }
            left++
        }
        for left <= right && len(oddMap) > len(evenMap) {
            if nums[left]%2 == 0 {
                evenMap[nums[left]]--
                if evenMap[nums[left]] == 0 {
                    delete(evenMap, nums[left])
                }
            } else {
                oddMap[nums[left]]--
                if oddMap[nums[left]] == 0 {
                    delete(oddMap, nums[left])
                }
            }
            left++
        }
        if len(evenMap) == len(oddMap) {
            if right-left+1 > maxLen {
                maxLen = right-left+1
            }
        }
    }
    return maxLen
}
# @lc code=end