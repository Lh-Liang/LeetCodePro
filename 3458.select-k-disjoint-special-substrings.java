# @lc app=leetcode id=3458 lang=java
# [3458] Select K Disjoint Special Substrings

# @lc code=start
class Solution {
    public boolean maxSubstringLength(String s, int k) {
        // Count occurrences of each character in the string
        Map<Character, Integer> charCount = new HashMap<>();
        for (char c : s.toCharArray()) {
            charCount.put(c, charCount.getOrDefault(c, 0) + 1);
        }

        // Count unique characters with frequency of exactly one
        int uniqueChars = 0;
        for (int count : charCount.values()) {
            if (count == 1) {
                uniqueChars++;
            }
        }

        // Check if we have at least k disjoint special substrings using unique characters
        return uniqueChars >= k;
    }
}
# @lc code=end