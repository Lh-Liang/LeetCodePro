#
# @lc app=leetcode id=3594 lang=golang
#
# [3594] Minimum Time to Transport All Individuals
#

# @lc code=start
import (
    "math"
)

func minTime(n int, k int, m int, time []int, mul []float64) float64 {
    if n == 1 {
        return float64(time[0]) * mul[0]
    }
    if k == 1 && n > 1 {
        return -1.0
    }
    type state struct {
        mask, stage, side int
    }
    memo := make(map[state]float64)
    full := (1 << n) - 1
    var dfs func(mask, stage, side int) float64
    dfs = func(mask, stage, side int) float64 {
        st := state{mask, stage, side}
        if v, ok := memo[st]; ok {
            return v
        }
        // If all crossed and boat at destination, done
        if mask == 0 && side == 1 {
            return 0.0
        }
        // Impossible state: all at start but boat at destination
        if mask == full && side == 1 {
            return math.Inf(1)
        }
        res := math.Inf(1)
        if side == 0 {
            // At start, try all valid groups of 1..k to cross
            var indices []int
            for i := 0; i < n; i++ {
                if mask&(1<<i) != 0 {
                    indices = append(indices, i)
                }
            }
            sz := len(indices)
            // Generate all combinations of 1 to k people
            var comb func(start, cnt int, group []int)
            comb = func(start, cnt int, group []int) {
                if cnt > 0 && cnt <= k {
                    // Verify group is valid
                    maxT := 0
                    for _, idx := range group {
                        if time[idx] > maxT {
                            maxT = time[idx]
                        }
                    }
                    crossTime := float64(maxT) * mul[stage]
                    nxtMask := mask
                    for _, idx := range group {
                        nxtMask ^= (1 << idx)
                    }
                    nxtStage := (stage + int(math.Floor(crossTime))%m) % m
                    // If all have crossed, boat now at destination
                    if nxtMask == 0 {
                        res = math.Min(res, crossTime+dfs(nxtMask, nxtStage, 1))
                    } else {
                        // Try all returns from group that just crossed
                        for _, retIdx := range group {
                            // Only allow return if person is at destination
                            returnTime := float64(time[retIdx]) * mul[nxtStage]
                            retStage := (nxtStage + int(math.Floor(returnTime))%m) % m
                            retMask := nxtMask | (1 << retIdx)
                            tmp := dfs(retMask, retStage, 0)
                            if tmp < math.Inf(1) {
                                res = math.Min(res, crossTime+returnTime+tmp)
                            }
                        }
                    }
                }
                if cnt == k || start == sz {
                    return
                }
                comb(start+1, cnt, group)
                comb(start+1, cnt+1, append(group, indices[start]))
            }
            comb(0, 0, []int{})
        } else {
            // At destination, if not all crossed, someone must return
            if mask == 0 {
                // All at dest, no further move
                return math.Inf(1)
            }
            // Only those at destination can return; those not in mask
            for i := 0; i < n; i++ {
                if mask&(1<<i) == 0 {
                    returnTime := float64(time[i]) * mul[stage]
                    retStage := (stage + int(math.Floor(returnTime))%m) % m
                    retMask := mask | (1 << i)
                    tmp := dfs(retMask, retStage, 0)
                    if tmp < math.Inf(1) {
                        res = math.Min(res, returnTime+tmp)
                    }
                }
            }
        }
        memo[st] = res
        return res
    }
    ans := dfs(full, 0, 0)
    if ans == math.Inf(1) {
        return -1.0
    }
    return math.Round(ans*1e5) / 1e5
}
# @lc code=end