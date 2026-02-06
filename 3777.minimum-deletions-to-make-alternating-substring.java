#
# @lc app=leetcode id=3777 lang=java
#
# [3777] Minimum Deletions to Make Alternating Substring
#
# @lc code=start
class Solution {
    public int[] minDeletions(String s, int[][] queries) {
        int n = s.length();
        char[] arr = s.toCharArray();
        int[] answer = new int[queries.length];
        // Build prefix sum of adjacent equals
        int[] prefix = new int[n];
        for (int i = 1; i < n; i++) {
            prefix[i] = prefix[i-1] + (arr[i]==arr[i-1]?1:0);
        }
        for (int qi = 0, ai = 0; qi < queries.length; qi++) {
            int[] q = queries[qi];
            if (q[0] == 1) {
                int j = q[1];
                arr[j] = arr[j]=='A'?'B':'A';
                // Only update prefix at j and j+1
                if (j > 0) {
                    prefix[j] = prefix[j-1] + (arr[j]==arr[j-1]?1:0);
                }
                for (int k = j+1; k < n && k <= j+1; k++) {
                    prefix[k] = prefix[k-1] + (arr[k]==arr[k-1]?1:0);
                }
            } else {
                int l = q[1], r = q[2];
                answer[ai++] = prefix[r] - (l>0?prefix[l]:0);
            }
        }
        // filter only type 2 answers
        int[] result = new int[(int) java.util.Arrays.stream(queries).filter(q->q[0]==2).count()];
        for (int i = 0, j = 0; i < queries.length; i++) {
            if (queries[i][0]==2) result[j++] = answer[i];
        }
        return result;
    }
}
# @lc code=end