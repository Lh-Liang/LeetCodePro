#
# @lc app=leetcode id=3387 lang=java
#
# [3387] Maximize Amount After Two Days of Conversions
#
# @lc code=start
import java.util.*;
class Solution {
    public double maxAmount(String initialCurrency, List<List<String>> pairs1, double[] rates1, List<List<String>> pairs2, double[] rates2) {
        // Helper: build bidirectional graph (adjacency map)
        Map<String, Map<String, Double>> buildGraph(List<List<String>> pairs, double[] rates) {
            Map<String, Map<String, Double>> graph = new HashMap<>();
            for (int i = 0; i < pairs.size(); ++i) {
                String from = pairs.get(i).get(0);
                String to = pairs.get(i).get(1);
                double rate = rates[i];
                graph.computeIfAbsent(from, x -> new HashMap<>()).put(to, rate);
                graph.computeIfAbsent(to, x -> new HashMap<>()).put(from, 1.0 / rate);
            }
            return graph;
        }
        // Helper: maximize currency using Bellman-Ford (log-multiplicative)
        Map<String, Double> maximize(Map<String, Map<String, Double>> graph, String start, double amount) {
            Map<String, Double> maxAmount = new HashMap<>();
            maxAmount.put(start, amount);
            Queue<String> queue = new LinkedList<>();
            queue.offer(start);
            Set<String> inQueue = new HashSet<>();
            inQueue.add(start);
            int steps = 0, V = graph.size();
            while (!queue.isEmpty() && steps < V * 2) {
                int sz = queue.size();
                for (int k = 0; k < sz; ++k) {
                    String cur = queue.poll();
                    inQueue.remove(cur);
                    double curAmt = maxAmount.get(cur);
                    if (!graph.containsKey(cur)) continue;
                    for (Map.Entry<String, Double> e : graph.get(cur).entrySet()) {
                        String next = e.getKey();
                        double rate = e.getValue();
                        double nxtAmt = curAmt * rate;
                        if (nxtAmt > maxAmount.getOrDefault(next, 0.0) + 1e-9) {
                            maxAmount.put(next, nxtAmt);
                            if (!inQueue.contains(next)) {
                                queue.offer(next);
                                inQueue.add(next);
                            }
                        }
                    }
                }
                steps++;
            }
            return maxAmount;
        }
        Map<String, Map<String, Double>> graph1 = buildGraph(pairs1, rates1);
        Map<String, Map<String, Double>> graph2 = buildGraph(pairs2, rates2);
        // Step 1: Max amounts on day 1
        Map<String, Double> day1 = maximize(graph1, initialCurrency, 1.0);
        // Step 2: For each currency after day 1, maximize on day 2
        double maxFinal = day1.getOrDefault(initialCurrency, 1.0); // Option: do nothing
        for (Map.Entry<String, Double> entry : day1.entrySet()) {
            String currency = entry.getKey();
            double amount = entry.getValue();
            Map<String, Double> day2 = maximize(graph2, currency, amount);
            // Try to convert back to initialCurrency (may be same as currency)
            double val = day2.getOrDefault(initialCurrency, 0.0);
            if (val > maxFinal) maxFinal = val;
        }
        return maxFinal;
    }
}
# @lc code=end