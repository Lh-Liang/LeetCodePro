#
# @lc app=leetcode id=3538 lang=golang
#
# [3538] Merge Operations for Minimum Travel Time
#

# @lc code=start
import (
    "math"
    "fmt"
    "strings"
)

func minTravelTime(l int, n int, k int, position []int, time []int) int {
    type state struct {
        timeKey string
        posKey string
        k int
    }
    memo := map[state]int{}

    // Helper to get a unique key for memoization
    getKey := func(arr []int) string {
        sb := strings.Builder{}
        for i, v := range arr {
            if i > 0 {
                sb.WriteByte(',')
            }
            sb.WriteString(fmt.Sprintf("%d", v))
        }
        return sb.String()
    }

    var dp func([]int, []int, int) int
    dp = func(posArr []int, timeArr []int, mergesLeft int) int {
        if mergesLeft == 0 {
            // Calculate total travel time
            total := 0
            for i := 0; i < len(timeArr); i++ {
                dist := posArr[i+1] - posArr[i]
                total += dist * timeArr[i]
            }
            return total
        }
        key := state{getKey(timeArr), getKey(posArr), mergesLeft}
        if val, exists := memo[key]; exists {
            return val
        }
        res := math.MaxInt32
        // Try all valid merges: can only merge indices 1..len-2 (can't merge endpoints)
        for i := 1; i < len(timeArr); i++ {
            // Merge time[i-1] and time[i] into time[i]
            newTime := make([]int, 0, len(timeArr)-1)
            newPos := make([]int, 0, len(posArr)-1)
            // Copy up to i-1
            for j := 0; j < i-1; j++ {
                newTime = append(newTime, timeArr[j])
            }
            for j := 0; j <= i-1; j++ {
                newPos = append(newPos, posArr[j])
            }
            // Merge: time[i] = time[i-1] + time[i], remove time[i-1], remove pos[i]
            newTime = append(newTime, timeArr[i-1]+timeArr[i])
            // Copy rest
            for j := i+1; j < len(timeArr); j++ {
                newTime = append(newTime, timeArr[j])
            }
            for j := i+1; j < len(posArr); j++ {
                newPos = append(newPos, posArr[j])
            }
            // Verify newTime and newPos alignment
            if len(newTime) == len(newPos)-1 {
                val := dp(newPos, newTime, mergesLeft-1)
                if val < res {
                    res = val
                }
            }
        }
        memo[key] = res
        return res
    }

    return dp(position, time, k)
}
# @lc code=end