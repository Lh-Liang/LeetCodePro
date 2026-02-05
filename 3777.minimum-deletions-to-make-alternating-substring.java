# @lc app=leetcode id=3777 lang=java
# [3777] Minimum Deletions to Make Alternating Substring
# @lc code=start
class Solution {
    public int[] minDeletions(String s, int[][] queries) {
        char[] chars = s.toCharArray();
        List<Integer> results = new ArrayList<>();
        
        for (int[] query : queries) {
            if (query[0] == 1) { // Flip operation
                int j = query[1];
                chars[j] = (chars[j] == 'A') ? 'B' : 'A';
            } else if (query[0] == 2) { // Compute operation
                int l = query[1];
                int r = query[2];
                int deletions = 0;
                for (int i = l + 1; i <= r; i++) {
                    if (chars[i] == chars[i - 1]) {
                        deletions++;
                    }
                }
                results.add(deletions);
            }
        }
        
        return results.stream().mapToInt(i -> i).toArray();
    }
}
# @lc code=end