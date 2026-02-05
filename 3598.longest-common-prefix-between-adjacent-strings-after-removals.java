# @lc code=start
class Solution {
    public int[] longestCommonPrefix(String[] words) {
        int n = words.length;
        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            int maxPrefixLength = 0;
            for (int j = 0; j < n - 1; j++) {
                if (j == i || j + 1 == i) continue;
                String word1 = words[j];
                String word2 = words[j + (j + 1 == i ? 2 : 1)];
                int prefixLength = commonPrefixLength(word1, word2);
                maxPrefixLength = Math.max(maxPrefixLength, prefixLength);
            }
            result[i] = maxPrefixLength;
        }
        return result;
    }
    private int commonPrefixLength(String s1, String s2) {
        int minLength = Math.min(s1.length(), s2.length());
        for (int k = 0; k < minLength; k++) {
            if (s1.charAt(k) != s2.charAt(k)) {
                return k;
            }
        }
        return minLength;
    } 
}
# @lc code=end