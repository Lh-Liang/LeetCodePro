#
# @lc app=leetcode id=3457 lang=golang
#
# [3457] Eat Pizzas!
#

# @lc code=start
func maxWeight(pizzas []int) int64 {
    n := len(pizzas)
    sort.Ints(pizzas)
    var totalWeight int64 = 0
    
    for i := 0; i < n; i += 4 {
        if (i/4)%2 == 0 { // Odd day (1-indexed) since i starts from 0
            totalWeight += int64(pizzas[i+3]) // Gain weight of Z
        } else { // Even day
            totalWeight += int64(pizzas[i+2]) // Gain weight of Y
        }
    }
    return totalWeight
}
# @lc code=end