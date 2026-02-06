#
# @lc app=leetcode id=3457 lang=java
#
# [3457] Eat Pizzas!
#
# @lc code=start
class Solution {
    public long maxWeight(int[] pizzas) {
        Arrays.sort(pizzas); // Sorts in ascending by default
        int n = pizzas.length;
        long totalWeight = 0;
        for (int i = 0; i < n / 4; i++) {
            totalWeight += pizzas[n - 1 - (i * 4)]; // Odd-day: max at Z position
            totalWeight += pizzas[n - 2 - (i * 4)]; // Even-day: second max at Y position
        }
        return totalWeight;
    }
}
# @lc code=end