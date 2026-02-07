#
# @lc app=leetcode id=3457 lang=golang
#
# [3457] Eat Pizzas!
#
# @lc code=start
import (
    "sort"
)
func maxWeight(pizzas []int) int64 {
    sort.Ints(pizzas)
    n := len(pizzas)
    var ans int64 = 0
    for i := 0; i < n; i += 4 {
        // group: pizzas[i], pizzas[i+1], pizzas[i+2], pizzas[i+3]
        // 1-indexed day: (i/4)+1
        if ((i/4)+1)%2 == 1 { // odd day
            ans += int64(pizzas[i+3])
        } else { // even day
            ans += int64(pizzas[i+2])
        }
    }
    return ans
}
# @lc code=end