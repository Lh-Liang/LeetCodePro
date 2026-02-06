#
# @lc app=leetcode id=3562 lang=java
#
# [3562] Maximum Profit from Trading Stocks with Discounts
#
# @lc code=start
class Solution {
    public int maxProfit(int n, int[] present, int[] future, int[][] hierarchy, int budget) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int[] relation : hierarchy) {
            graph.computeIfAbsent(relation[0], k -> new ArrayList<>()).add(relation[1]);
        }
        int[] dp = new int[n + 1]; // Profit array initialized to store profits per employee
        boolean[] discountApplied = new boolean[n + 1]; // Track if discount is applied for an employee
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b) -> Integer.compare(b[1],a[1])); // Max heap based on profit
        for (int i = 0; i < n; i++) {
            int profitWithoutDiscount = Math.max(0, future[i] - present[i]);
            pq.offer(new int[]{i + 1, profitWithoutDiscount}); // Offering initial profits without discounts
        }
        while (!pq.isEmpty() && budget > 0) {
            int[] top = pq.poll();
            int empId = top[0];
            int profit = top[1];
            if (present[empId - 1] <= budget && !discountApplied[empId]) { // Check if purchase is possible without exceeding budget 
                budget -= present[empId - 1]; // Deduct from budget 
                dp[empId] += profit; 
                if (graph.containsKey(empId)) { // Apply discounts to subordinates 
                    for (int sub : graph.get(empId)) { 
                        if (!discountApplied[sub]) { 
                            discountApplied[sub] = true; " Calculate discounted prices and update profits " }}}}}return Arrays.stream(dp).sum();} } # @lc code=end