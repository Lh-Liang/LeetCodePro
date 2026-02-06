#
# @lc app=leetcode id=3488 lang=java
#
# [3488] Closest Equal Element Queries
#
# @lc code=start
import java.util.*;
class Solution {
    public List<Integer> solveQueries(int[] nums, int[] queries) {
        int n = nums.length;
        Map<Integer, List<Integer>> valToIndices = new HashMap<>();
        for (int i = 0; i < n; i++) {
            valToIndices.computeIfAbsent(nums[i], k -> new ArrayList<>()).add(i);
        }
        List<Integer> res = new ArrayList<>();
        for (int q : queries) {
            int val = nums[q];
            List<Integer> indices = valToIndices.get(val);
            if (indices.size() == 1) {
                res.add(-1);
                continue;
            }
            int pos = Collections.binarySearch(indices, q);
            // pos should always be found as q is in indices
            int before = (pos - 1 + indices.size()) % indices.size();
            int after = (pos + 1) % indices.size();
            int dist1 = Math.min(Math.abs(indices.get(before) - q), n - Math.abs(indices.get(before) - q));
            int dist2 = Math.min(Math.abs(indices.get(after) - q), n - Math.abs(indices.get(after) - q));
            int minDist = Math.min(dist1, dist2);
            res.add(minDist);
        }
        return res;
    }
}
# @lc code=end