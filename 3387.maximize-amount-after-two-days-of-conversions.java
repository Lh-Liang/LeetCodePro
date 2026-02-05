#
# @lc app=leetcode id=3387 lang=java
#
# [3387] Maximize Amount After Two Days of Conversions
#

# @lc code=start
import java.util.*;

class Solution {
    public double maxAmount(String initialCurrency, List<List<String>> pairs1, double[] rates1, List<List<String>> pairs2, double[] rates2) {
        // Create graphs for both days using adjacency lists
        Map<String, Map<String, Double>> graphDay1 = createGraph(pairs1, rates1);
        Map<String, Map<String, Double>> graphDay2 = createGraph(pairs2, rates2);
        
        // Maximize conversion from initialCurrency using Day 1's conversions
        Map<String, Double> maxAmountsDay1 = new HashMap<>();
        maxAmountsDay1.put(initialCurrency, 1.0);
        dfsMaxConversion(initialCurrency, maxAmountsDay1, graphDay1);
        
        // Maximize returning to initialCurrency using Day 2's conversions
        double maxAmount = 0.0;
        for (String currency : maxAmountsDay1.keySet()) {
            Map<String, Double> amountsDay2 = new HashMap<>();
            amountsDay2.put(currency, maxAmountsDay1.get(currency));
            dfsMaxConversion(currency, amountsDay2, graphDay2);
            if (amountsDay2.containsKey(initialCurrency)) {
                maxAmount = Math.max(maxAmount, amountsDay2.get(initialCurrency));
            }
        }
        
        return maxAmount;
    }
    
    private Map<String, Map<String, Double>> createGraph(List<List<String>> pairs, double[] rates) {
        Map<String, Map<String, Double>> graph = new HashMap<>();
        for (int i = 0; i < pairs.size(); i++) {
            String start = pairs.get(i).get(0);
            String end = pairs.get(i).get(1);
            double rate = rates[i];
            graph.computeIfAbsent(start, k -> new HashMap<>()).put(end, rate);
            // Add reverse conversion
            graph.computeIfAbsent(end, k -> new HashMap<>()).put(start, 1 / rate);
        }
        return graph;
    }
    
    private void dfsMaxConversion(String current,
                                    Map<String, Double> maxAmounts,
                                    Map<String, Map<String, Double>> graph) {
        if (!graph.containsKey(current)) return;
        for (Map.Entry<String, Double> entry : graph.get(current).entrySet()) {
            String nextCurrency = entry.getKey();
            double rate = entry.getValue();
            double newAmount = maxAmounts.get(current) * rate;
            if (newAmount > maxAmounts.getOrDefault(nextCurrency, 0.0)) {
                maxAmounts.put(nextCurrency,newAmount);
dfsMaxConversion(nextCurrency,maxAmounts ,graph);}}}}