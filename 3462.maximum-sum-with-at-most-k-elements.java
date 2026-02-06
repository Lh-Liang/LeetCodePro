#
# @lc app=leetcode id=3462 lang=java
#
# [3462] Maximum Sum With at Most K Elements
#
# @lc code=start
class Solution {
    public long maxSum(int[][] grid, int[] limits, int k) {
        List<Integer> candidates = new ArrayList<>();
        for (int i = 0; i < grid.length; i++) {
            int[] row = grid[i];
            Arrays.sort(row); // ascending
            int cnt = Math.min(limits[i], row.length);
            for (int j = 0; j < cnt; j++) {
                candidates.add(row[row.length - 1 - j]); // pick largest cnt elements
            }
        }
        Collections.sort(candidates, Collections.reverseOrder());
        long sum = 0;
        for (int i = 0; i < Math.min(k, candidates.size()); i++) {
            sum += candidates.get(i);
        }
        return sum;
    }
}
# @lc code=end