#
# @lc app=leetcode id=3441 lang=java
#
# [3441] Minimum Cost Good Caption
#

# @lc code=start
class Solution {
    public String minCostGoodCaption(String caption) {
        int n = caption.length();
        if (n % 3 != 0) return "";
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i += 3) {
            int minCost = Integer.MAX_VALUE;
            char bestChar = 'z';
            for (char c = 'a'; c <= 'z'; c++) {
                int cost = 0;
                for (int j = 0; j < 3; j++) {
                    if (caption.charAt(i + j) == c) continue;
                    cost += Math.abs(caption.charAt(i + j) - c);
                }
                if (cost < minCost || (cost == minCost && c < bestChar)) {
                    minCost = cost;
                    bestChar = c;
                }
            }
            for (int j = 0; j < 3; j++) sb.append(bestChar);
        }
        return sb.toString();
    }
}
# @lc code=end