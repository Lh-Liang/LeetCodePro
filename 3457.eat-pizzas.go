#
# @lc app=leetcode id=3457 lang=golang
#
# [3457] Eat Pizzas!
#
# @lc code=start
func maxWeight(pizzas []int) int64 {
    // Sort pizzas to facilitate optimal selection
    sort.Ints(pizzas)
    n := len(pizzas)
    totalWeight := int64(0)
    // Iterate through batches of 4 pizzas each day
    for i := 0; i < n; i += 4 {
        if (i/4)%2 == 0 {
            // Odd-numbered days: Gain weight Z (maximum of 4)
            totalWeight += int64(pizzas[i+3])
        } else {
            // Even-numbered days: Gain weight Y (second maximum of 4)
            totalWeight += int64(pizzas[i+2])
        }
    }
    return totalWeight
}
# @lc code=end