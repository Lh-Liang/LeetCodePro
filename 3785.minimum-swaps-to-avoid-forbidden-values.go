#
# @lc app=leetcode id=3785 lang=golang
#
# [3785] Minimum Swaps to Avoid Forbidden Values
#

# @lc code=start
func minSwaps(nums []int, forbidden []int) int {
    n := len(nums)
    // Step 1: Modular conflict detection
    conflicts := make([]int, 0)
    for i := 0; i < n; i++ {
        if nums[i] == forbidden[i] {
            conflicts = append(conflicts, i)
        }
    }
    if len(conflicts) == 0 {
        return 0
    }
    // Step 2: Explicitly check for impossible cases
    cntNum, cntForbidden := make(map[int]int), make(map[int]int)
    for i := 0; i < n; i++ {
        cntNum[nums[i]]++
        if nums[i] == forbidden[i] {
            cntForbidden[nums[i]]++
        }
    }
    for v, cnt := range cntNum {
        if cnt == cntForbidden[v] {
            return -1
        }
    }
    // Step 3: Dependency modeling and swap planning
    used := make([]bool, n)
    arr := make([]int, n)
    copy(arr, nums)
    swaps := 0
    // Helper: modular verification
    verify := func(a []int) bool {
        for i := 0; i < n; i++ {
            if a[i] == forbidden[i] {
                return false
            }
        }
        return true
    }
    for _, i := range conflicts {
        if used[i] || arr[i] != forbidden[i] {
            continue
        }
        found := false
        for j := 0; j < n; j++ {
            if i == j || used[j] {
                continue
            }
            if arr[j] != forbidden[i] && arr[i] != forbidden[j] && arr[j] != forbidden[j] {
                arr[i], arr[j] = arr[j], arr[i]
                used[i], used[j] = true, true
                swaps++
                found = true
                // Step 4: Explicitly verify after operation
                if !verify(arr) {
                    return -1
                }
                break
            }
        }
        if !found {
            for _, j := range conflicts {
                if i == j || used[j] {
                    continue
                }
                if arr[j] != forbidden[i] && arr[i] != forbidden[j] {
                    arr[i], arr[j] = arr[j], arr[i]
                    used[i], used[j] = true, true
                    swaps++
                    // Step 4: Explicitly verify after operation
                    if !verify(arr) {
                        return -1
                    }
                    found = true
                    break
                }
            }
        }
        if !found {
            return -1
        }
    }
    // Step 5: Final global verification
    if !verify(arr) {
        return -1
    }
    return swaps
}
# @lc code=end