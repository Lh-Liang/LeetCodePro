#
# @lc app=leetcode id=3413 lang=java
#
# [3413] Maximum Coins From K Consecutive Bags
#
# @lc code=start
import java.util.*;

class Solution {
    public long maximumCoins(int[][] coins, int k) {
        // Step 1: Use a map to apply range updates efficiently
        Map<Integer, Long> delta = new TreeMap<>();
        for (int[] coin : coins) {
            int li = coin[0], ri = coin[1], ci = coin[2];
            delta.put(li, delta.getOrDefault(li, 0L) + ci);
            delta.put(ri + 1, delta.getOrDefault(ri + 1, 0L) - ci);
        }
        
        // Step 2: Calculate prefix sums and use sliding window to find max sum for k consecutive positions
        long currentSum = 0;
        long maxCoins = 0;
        LinkedList<Long> windowSums = new LinkedList<>();
        int lastPosition = -1; // Track the last position processed
        
        for (Map.Entry<Integer, Long> entry : delta.entrySet()) {
            int pos = entry.getKey();
            long change = entry.getValue();
            
            if (lastPosition != -1 && pos > lastPosition + 1) {
                // Fill gaps between positions if they exist
                while (windowSums.size() < k && lastPosition < pos - 1) {
                    windowSums.add(currentSum);
                    maxCoins = Math.max(maxCoins, currentSum);
                    lastPosition++;
                }
            }
            
            currentSum += change; // Apply change at this position
            windowSums.add(currentSum);
            if (windowSums.size() > k) {
                currentSum -= windowSums.poll(); // Slide the window forward by removing oldest entry
            }
            
            maxCoins = Math.max(maxCoins, currentSum); // Update max coins found so far
            lastPosition = pos;
        }
        return maxCoins; 
    }
}
# @lc code=end