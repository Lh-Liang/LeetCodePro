#
# @lc app=leetcode id=3457 lang=java
#
# [3457] Eat Pizzas!
#
# @lc code=start
class Solution {
    public long maxWeight(int[] pizzas) {
        Arrays.sort(pizzas);
        long totalWeight = 0;
        int n = pizzas.length;
        for (int i = 0; i < n; i += 4) {
            // Odd day: take Z (pizzas[i+3])
            if ((i / 4) % 2 == 0) {
                totalWeight += pizzas[i + 3];
            } else { // Even day: take Y (pizzas[i+2])
                totalWeight += pizzas[i + 2];
            }
        }
        return totalWeight;
    }
}
# @lc code=end