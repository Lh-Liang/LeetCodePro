#
# @lc app=leetcode id=3509 lang=golang
#
# [3509] Maximum Product of Subsequences With an Alternating Sum Equal to K
#
# @lc code=start
func maxProduct(nums []int, k int, limit int) int {
    type state struct {
        sum   int
        parity int
    }
    dp := make(map[state]int)
    n := len(nums)
    for i := 0; i < n; i++ {
        ndp := make(map[state]int)
        // Start a new subsequence with nums[i]
        s := nums[i]
        p := 0
        prod := nums[i]
        if prod <= limit {
            st := state{s, p}
            if ndp[st] < prod {
                ndp[st] = prod
            }
        }
        // Try to extend all existing subsequences
        for key, val := range dp {
            // Not picking nums[i]
            if ndp[key] < val {
                ndp[key] = val
            }
            // Picking nums[i]
            nparity := (key.parity + 1) % 2
            if key.parity == 0 {
                nsum := key.sum - nums[i]
                nprod := val * nums[i]
                if nprod <= limit {
                    st := state{nsum, nparity}
                    if ndp[st] < nprod {
                        ndp[st] = nprod
                    }
                }
            } else {
                nsum := key.sum + nums[i]
                nprod := val * nums[i]
                if nprod <= limit {
                    st := state{nsum, nparity}
                    if ndp[st] < nprod {
                        ndp[st] = nprod
                    }
                }
            }
        }
        dp = ndp
    }
    res := -1
    for key, val := range dp {
        if key.sum == k && val > res {
            res = val
        }
    }
    return res
}
# @lc code=end