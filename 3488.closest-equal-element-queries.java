//
// @lc app=leetcode id=3488 lang=java
//
// [3488] Closest Equal Element Queries
//

// @lc code=start
import java.util.*;
class Solution {
    public List<Integer> solveQueries(int[] nums, int[] queries) {
        int n = nums.length;
        Map<Integer, List<Integer>> valueToIndices = new HashMap<>();
        for (int i = 0; i < n; i++) {
            valueToIndices.computeIfAbsent(nums[i], k -> new ArrayList<>()).add(i);
        }
        List<Integer> res = new ArrayList<>();
        for (int q : queries) {
            int val = nums[q];
            List<Integer> idxList = valueToIndices.get(val);
            if (idxList.size() == 1) {
                res.add(-1);
                continue;
            }
            // idxList is sorted; use binary search to find position of q
            int pos = Collections.binarySearch(idxList, q);
            if (pos < 0) pos = -pos - 1; // Should not happen, but safe
            int sz = idxList.size();
            int minDist = Integer.MAX_VALUE;
            // Check previous and next neighbor, with circular wrap
            int prevIdx = (pos - 1 + sz) % sz;
            int nextIdx = (pos + 1) % sz;
            int[] candidates = {idxList.get(prevIdx), idxList.get(nextIdx)};
            for (int candidate : candidates) {
                if (candidate != q) {
                    int dist = Math.abs(q - candidate);
                    dist = Math.min(dist, n - dist); // circular distance
                    minDist = Math.min(minDist, dist);
                }
            }
            // Ensure result is valid and not from self-comparison
            res.add(minDist == Integer.MAX_VALUE ? -1 : minDist);
        }
        return res;
    }
}
// @lc code=end