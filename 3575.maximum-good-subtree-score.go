#
# @lc app=leetcode id=3575 lang=golang
#
# [3575] Maximum Good Subtree Score
#

# @lc code=start
func goodSubtreeSum(vals []int, par []int) int {
    const MOD = 1_000_000_007
    n := len(vals)
    tree := make([][]int, n)
    for i := 1; i < n; i++ {
        tree[par[i]] = append(tree[par[i]], i)
    }

    // Helper to get the bitmask for a value
    digitMask := func(val int) int {
        mask := 0
        for val > 0 {
            d := val % 10
            if (mask&(1<<d)) != 0 {
                return -1 // duplicate
            }
            mask |= 1 << d
            val /= 10
        }
        return mask
    }

    // For each node: map[used_digit_mask]max_sum
    var dfs func(int) map[int]int
    maxScore := make([]int, n)

    dfs = func(u int) map[int]int {
        curMask := digitMask(vals[u])
        res := make(map[int]int)
        if curMask != -1 {
            res[curMask] = vals[u]
        }
        for _, v := range tree[u] {
            child := dfs(v)
            newRes := make(map[int]int)
            // Don't combine: just keep original
            for mask, sum := range res {
                if newRes[mask] < sum {
                    newRes[mask] = sum
                }
            }
            // Combine child with current
            for cm, cs := range child {
                // Option 1: take only child
                if newRes[cm] < cs {
                    newRes[cm] = cs
                }
                // Option 2: combine with current
                for mask, sum := range res {
                    if mask&cm == 0 {
                        if newRes[mask|cm] < sum+cs {
                            newRes[mask|cm] = sum + cs
                        }
                    }
                }
            }
            res = newRes
        }
        // Find max for this node
        best := 0
        for _, v := range res {
            if v > best {
                best = v
            }
        }
        maxScore[u] = best
        return res
    }

    dfs(0)
    ans := 0
    for _, v := range maxScore {
        ans = (ans + v) % MOD
    }
    return ans
}
# @lc code=end