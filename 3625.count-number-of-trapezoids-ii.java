#
# @lc app=leetcode id=3625 lang=java
#
# [3625] Count Number of Trapezoids II
#

# @lc code=start
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import java.util.Arrays;

class Solution {
    public int countTrapezoids(int[][] points) {
        int n = points.length;
        if (n < 4) return 0;
        Set<String> uniqueTrapezoids = new HashSet<>();
        Map<String, Set<int[]>> slopeMap = new HashMap<>();
        
        // Calculate slopes among all point pairs and group them
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                String slope = calculateSlope(points[i], points[j]);
                
                if (!slopeMap.containsKey(slope)) {
                    slopeMap.put(slope, new HashSet<>());
                }
                slopeMap.get(slope).add(new int[]{i, j});
            }
        }
        
        // Check possible trapezoid formations
        for (String slope : slopeMap.keySet()) {
            Set<int[]> linePairs = slopeMap.get(slope);
            Integer[] indices = linePairs.stream().flatMapToInt(Arrays::stream).distinct().boxed().toArray(Integer[]::new);
            int len = indices.length;
            if (len >= 4) {
                for (int a = 0; a < len - 3; a++) {
                    for (int b = a + 1; b < len - 2; b++) {
                        for (int c = b + 1; c < len - 1; c++) {
                            for (int d = c + 1; d < len; d++) {
                                int[] quartet = {indices[a], indices[b], indices[c], indices[d]};
                                String configKey = getConfigurationKey(quartet);
                                uniqueTrapezoids.add(configKey);
                            }
                        }
                    }
                }	 		}		}		return uniqueTrapezoids.size();    		// Return size of the unique trapezoid set as result    	}	    	private String calculateSlope(int[] p1, int[] p2) {      int dy = p2[1] - p1[1];      int dx = p2[0] - p1[0];      // Handle vertical lines by defining consistent representation      if (dx == 0) return dy > 0 ? "Infinity" : "-Infinity";      int gcdValue = gcd(dy, dx);     // Use GCD to reduce dy and dx      dy /= gcdValue;       dx /= gcdValue;   // Maintain consistency in representation by ensuring positive denominator      if (dx < 0) {          dy *= -1;          dx *= -1;      }      return dy + "/" + dx;}    private int gcd(int a, int b) {   // Recursive method to find greatest common divisor     if(b == 0) return Math.abs(a);   // Base condition for recursion end     return gcd(b, a % b);}   private String getConfigurationKey(int[] quartet) {   Arrays.sort(quartet);   // Sort quartet array     return Arrays.toString(quartet);   // Return sorted array as string } } # @lc code=end