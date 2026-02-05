#
# @lc app=leetcode id=3777 lang=java
#
# [3777] Minimum Deletions to Make Alternating Substring
#
# @lc code=start
class Solution {
    public int[] minDeletions(String s, int[][] queries) {
        char[] arr = s.toCharArray();
        List<Integer> answers = new ArrayList<>();
        for (int[] query : queries) {
            if (query[0] == 1) {
                int idx = query[1];
                arr[idx] = (arr[idx] == 'A') ? 'B' : 'A';
            } else {
                int l = query[1], r = query[2];
                int minDel = 0;
                for (int i = l + 1; i <= r; ++i) {
                    if (arr[i] == arr[i - 1]) minDel++;
                }
                answers.add(minDel);
            }
        }
        int[] res = new int[answers.size()];
        for (int i = 0; i < answers.size(); ++i) res[i] = answers.get(i);
        return res;
    }
}
# @lc code=end