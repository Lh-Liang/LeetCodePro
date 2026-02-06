#
# @lc app=leetcode id=3387 lang=java
#
# [3387] Maximize Amount After Two Days of Conversions
#

# @lc code=start
class Solution {
    public double maxAmount(String initialCurrency, List<List<String>> pairs1, double[] rates1, List<List<String>> pairs2, double[] rates2) {
        // Step 1: Create a map to store maximum amounts achievable for each currency on Day 1.
        Map<String, Double> day1Amounts = new HashMap<>();
        day1Amounts.put(initialCurrency, 1.0);
        
        // Step 2: Process all conversions on Day 1 to fill day1Amounts.
        for (int i = 0; i < pairs1.size(); i++) {
            String start = pairs1.get(i).get(0);
            String target = pairs1.get(i).get(1);
            double rate = rates1[i];
            if (day1Amounts.containsKey(start)) {
                double newAmount = day1Amounts.get(start) * rate;
                day1Amounts.put(target, Math.max(day1Amounts.getOrDefault(target, 0.0), newAmount));
            }
        }
        
        // Step 3: Initialize map for Day 2 amounts starting with Day 1 results.
        Map<String, Double> day2Amounts = new HashMap<>(day1Amounts);
        
        // Step 4: Process all conversions on Day 2 using updated amounts from Day 1.
        for (int i = 0; i < pairs2.size(); i++) {
            String start = pairs2.get(i).get(0);
            String target = pairs2.get(i).get(1);
            double rate = rates2[i];
            if (day2Amounts.containsKey(start)) {
                double newAmount = day2Amounts.get(start) * rate;
                day2Amounts.put(target, Math.max(day2Amounts.getOrDefault(target, 0.0), newAmount));
            }
        }
        
        // Step 5: Return maximum amount that can be converted back to initialCurrency.
        return day2Amounts.getOrDefault(initialCurrency, 0.0);
    }
}
# @lc code=end