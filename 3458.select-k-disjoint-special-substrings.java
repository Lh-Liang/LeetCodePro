#
# @lc app=leetcode id=3458 lang=java
#
# [3458] Select K Disjoint Special Substrings
#

# @lc code=start
class Solution {
    public boolean maxSubstringLength(String s, int k) {
        // Step 1: Calculate frequency of each character in the string
        Map<Character, Integer> frequency = new HashMap<>();
        for (char c : s.toCharArray()) {
            frequency.put(c, frequency.getOrDefault(c, 0) + 1);
        }
        
        // Step 2: Count unique characters that appear only once (can form special substrings)
        int uniqueCount = 0;
        for (int count : frequency.values()) {
            if (count == 1) {
                uniqueCount++;
            }
        }
        
        // Step 3: Check if we have enough unique characters to form k disjoint special substrings
        return uniqueCount >= k;
    }
}
# @lc code=end