#
# @lc app=leetcode id=3630 lang=golang
#
# [3630] Partition Array for Maximum XOR and AND
#
# @lc code=start
func maximizeXorAndXor(nums []int) int64 {
    n := len(nums)
    type key struct {
        i, xorA, andB, xorC int
    }
    memo := make(map[key]int64)
    var dfs func(i int, xorA int, andB int, xorC int) int64
    dfs = func(i int, xorA int, andB int, xorC int) int64 {
        k := key{i, xorA, andB, xorC}
        if val, exists := memo[k]; exists {
            return val
        }
        if i == n {
            ab := 0
            if andB != -1 {
                ab = andB
            }
            return int64(xorA + ab + xorC)
        }
        // Assign nums[i] to A
        resA := dfs(i+1, xorA^nums[i], andB, xorC)
        // Assign nums[i] to B
        newAndB := nums[i]
        if andB != -1 {
            newAndB = andB & nums[i]
        }
        resB := dfs(i+1, xorA, newAndB, xorC)
        // Assign nums[i] to C
        resC := dfs(i+1, xorA, andB, xorC^nums[i])
        maxRes := resA
        if resB > maxRes {
            maxRes = resB
        }
        if resC > maxRes {
            maxRes = resC
        }
        memo[k] = maxRes
        return maxRes
    }
    return dfs(0, 0, -1, 0)
}
# @lc code=end