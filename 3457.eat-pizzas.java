#
# @lc app=leetcode id=3457 lang=java
#
# [3457] Eat Pizzas!
#
# @lc code=start
class Solution {
    public long maxWeight(int[] pizzas) {
        Arrays.sort(pizzas);
        int n = pizzas.length;
        long total = 0;
        int days = n / 4;
        for (int d = 0; d < days; ++d) {
            int idx = d * 4;
            if ((d + 1) % 2 == 1) { // odd day (1-indexed)
                total += pizzas[idx + 3]; // Z
            } else {
                total += pizzas[idx + 2]; // Y
            }
        }
        return total;
    }
}
# @lc code=end