#
# @lc app=leetcode id=3704 lang=golang
#
# [3704] Count No-Zero Pairs That Sum to N
#

# @lc code=start
import (
    "strconv"
)

func countNoZeroPairs(n int64) int64 {
    s := strconv.FormatInt(n, 10)
    m := len(s)
    memo := make(map[[3]int]int64)

    // dp(pos, carry, tight):
    // pos = current digit position from right (0 = least significant)
    // carry = carry from previous (right) digit
    // tight = 1 if current prefix matches n exactly, 0 otherwise
    var dp func(pos int, carry int, tight int) int64
    dp = func(pos int, carry int, tight int) int64 {
        if pos == m {
            if carry == 0 {
                return 1
            }
            return 0
        }
        key := [3]int{pos, carry, tight}
        if v, ok := memo[key]; ok {
            return v
        }
        var res int64 = 0
        maxD := int(s[m-1-pos] - '0')
        for da := 1; da <= 9; da++ {
            for db := 1; db <= 9; db++ {
                sum := da + db + carry
                digit := sum % 10
                newCarry := sum / 10
                if tight == 1 {
                    if digit > maxD {
                        continue
                    }
                    if digit == maxD {
                        res += dp(pos+1, newCarry, 1)
                    } else {
                        res += dp(pos+1, newCarry, 0)
                    }
                } else {
                    res += dp(pos+1, newCarry, 0)
                }
            }
        }
        memo[key] = res
        return res
    }
    // Verification step: ensure state and transitions are correct for the sample input (can be commented out in production)
    // _ = dp(0, 0, 1) // e.g., for debugging
    return dp(0, 0, 1)
}
# @lc code=end