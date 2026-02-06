#
# @lc app=leetcode id=3458 lang=java
#
# [3458] Select K Disjoint Special Substrings
#
# @lc code=start
class Solution {
    public boolean maxSubstringLength(String s, int k) {
        int n = s.length();
        int[] first = new int[26];
        int[] last = new int[26];
        for (int i = 0; i < 26; ++i) {
            first[i] = n;
            last[i] = -1;
        }
        for (int i = 0; i < n; ++i) {
            int idx = s.charAt(i) - 'a';
            first[idx] = Math.min(first[idx], i);
            last[idx] = Math.max(last[idx], i);
        }
        List<int[]> intervals = new ArrayList<>();
        for (int i = 0; i < 26; ++i) {
            if (first[i] < n && last[i] > -1) {
                intervals.add(new int[]{first[i], last[i]});
            }
        }
        // Merge intervals to define special substrings
        List<int[]> merged = new ArrayList<>();
        intervals.sort((a, b) -> Integer.compare(a[0], b[0]));
        int i = 0;
        while (i < intervals.size()) {
            int l = intervals.get(i)[0], r = intervals.get(i)[1];
            int j = i + 1;
            boolean expanded;
            do {
                expanded = false;
                for (int x = i + 1; x < intervals.size(); ++x) {
                    if (intervals.get(x)[0] > r) break;
                    if (intervals.get(x)[1] > r) {
                        r = intervals.get(x)[1];
                        expanded = true;
                    }
                }
            } while (expanded);
            if (!(l == 0 && r == n - 1)) {
                merged.add(new int[]{l, r});
            }
            // Skip to the next non-overlapping interval
            while (i < intervals.size() && intervals.get(i)[0] <= r) ++i;
        }
        // Greedily select disjoint substrings
        merged.sort((a, b) -> Integer.compare(a[1], b[1]));
        int count = 0, end = -1;
        for (int[] interval : merged) {
            if (interval[0] > end) {
                count++;
                end = interval[1];
            }
        }
        return count >= k;
    }
}
# @lc code=end