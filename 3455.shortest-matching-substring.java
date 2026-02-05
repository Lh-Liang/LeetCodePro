# @lc code=start
class Solution {
    public int shortestMatchingSubstring(String s, String p) {
        // Find indices of '*' in pattern p
        int firstStar = p.indexOf('*');
        int secondStar = p.indexOf('*', firstStar + 1);
        if (secondStar == -1) return -1; // Ensure exactly two '*'
        
        // Extract segments based on '*' positions
        String prefix = p.substring(0, firstStar);
        String middle = p.substring(firstStar + 1, secondStar);
        String suffix = p.substring(secondStar + 1);

        int minLength = Integer.MAX_VALUE;

        // Efficient search using two pointers
        for (int i = 0; i <= s.length() - prefix.length(); i++) {
            if (s.startsWith(prefix, i)) {
                for (int j = i + prefix.length(); j <= s.length() - suffix.length(); j++) {
                    if ((middle.isEmpty() || s.substring(i + prefix.length(), j).contains(middle)) && s.startsWith(suffix, j)) {
                        minLength = Math.min(minLength, j + suffix.length() - i);
                        break; // Stop further checks once we find a valid match
                    }
                }
            }
        }

        return minLength == Integer.MAX_VALUE ? -1 : minLength;
    }
}
# @lc code=end