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
        long res = 0;
        int days = n / 4;
        for (int i = 0; i < days; ++i) {
            int idx = n - 4 * i;
            if ((i & 1) == 0) { // odd-numbered day (1-indexed)
                res += pizzas[idx - 1]; // largest (Z)
            } else { // even-numbered day
                res += pizzas[idx - 2]; // second largest (Y)
            }
        }
        return res;
    }
}
# @lc code=end