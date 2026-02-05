#
# @lc app=leetcode id=3387 lang=java
#
# [3387] Maximize Amount After Two Days of Conversions
#

# @lc code=start
import java.util.*;
class Solution {
    public double maxAmount(String initialCurrency, List<List<String>> pairs1, double[] rates1, List<List<String>> pairs2, double[] rates2) {
        // Step 1: Build graph for both days
        Map<String, Map<String, Double>> g1 = buildGraph(pairs1, rates1);
        Map<String, Map<String, Double>> g2 = buildGraph(pairs2, rates2);
        // Step 2: Propagate max on day 1
        Map<String, Double> day1 = maximize(initialCurrency, g1);
        // Step 3: For each resulting currency after day 1, use as sources for day 2
        double max = 0.0;
        for (Map.Entry<String, Double> entry : day1.entrySet()) {
            Map<String, Double> day2 = maximize(entry.getKey(), g2, entry.getValue());
            max = Math.max(max, day2.getOrDefault(initialCurrency, 0.0));
        }
        return max;
    }
    // Build graph with both directions
    private Map<String, Map<String, Double>> buildGraph(List<List<String>> pairs, double[] rates) {
        Map<String, Map<String, Double>> graph = new HashMap<>();
        for (int i = 0; i < pairs.size(); ++i) {
            String a = pairs.get(i).get(0), b = pairs.get(i).get(1);
            double rate = rates[i];
            graph.computeIfAbsent(a, k -> new HashMap<>()).put(b, rate);
            graph.computeIfAbsent(b, k -> new HashMap<>()).put(a, 1.0 / rate);
        }
        return graph;
    }
    // BFS-style max propagation (default start=1.0)
    private Map<String, Double> maximize(String start, Map<String, Map<String, Double>> graph) {
        return maximize(start, graph, 1.0);
    }
    private Map<String, Double> maximize(String start, Map<String, Map<String, Double>> graph, double startAmount) {
        Map<String, Double> maxAmounts = new HashMap<>();
        Queue<String> q = new LinkedList<>();
        maxAmounts.put(start, startAmount);
        q.offer(start);
        while (!q.isEmpty()) {
            String curr = q.poll();
            double currAmt = maxAmounts.get(curr);
            if (!graph.containsKey(curr)) continue;
            for (Map.Entry<String, Double> e : graph.get(curr).entrySet()) {
                String next = e.getKey();
                double rate = e.getValue();
                double newAmt = currAmt * rate;
                if (newAmt > maxAmounts.getOrDefault(next, 0.0) + 1e-9) {
                    maxAmounts.put(next, newAmt);
                    q.offer(next);
                }
            }
        }
        return maxAmounts;
    }
}
# @lc code=end