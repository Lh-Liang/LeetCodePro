#
# @lc app=leetcode id=3501 lang=java
#
# [3501] Maximize Active Section with Trade II
#

# @lc code=start
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> maxActiveSectionsAfterTrade(String s, int[][] queries) {
        List<Integer> results = new ArrayList<>();
        for (int[] query : queries) {
            int li = query[0];
            int ri = query[1];
            String t = "1" + s.substring(li, ri + 1) + "1"; // Augmenting string with '1' on both ends
            int initialActiveSections = calculateInitialActiveSections(t);
            int maxActiveSections = maximizeByTrade(t, initialActiveSections);
            results.add(maxActiveSections);
        }
        return results;
    }
    
    private int calculateInitialActiveSections(String t) {
        int count = 0;
        boolean isActive = false;
        for (int i = 0; i < t.length(); i++) {
            if (t.charAt(i) == '1') {
                if (!isActive) {
                    isActive = true;
                    count++;
                }
            } else {
                isActive = false;
            }
        }
        return count; // Return total number of initial active sections.
    } 
    
    private int maximizeByTrade(String t, int initialActiveSections) { 
        int maxGain = 0; 
        boolean insideZeros = false; \
b        for (int i = 1; i < t.length() - 1; i++) { // Start from 1 and end at length - 2 to avoid augmented '1's \b            if (t.charAt(i) == '0') { \b                if (!insideZeros && t.charAt(i - 1) == '1' && t.charAt(i + 1) == '0') { \b                    insideZeros = true; \b                } else if (insideZeros && t.charAt(i + 1) == '0') { \b                    maxGain += 2; // Extend zero block gain potential \b                } else if (insideZeros && t.charAt(i + 1) == '1') { \b                    insideZeros = false; \b                    maxGain += 2; // End of zero block, evaluate gain \b                } \b            } else { \b                insideZeros = false; \b           } \b       } \b       return initialActiveSections + maxGain / 2; \b   } \b} # @lc code=end