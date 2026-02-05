//
// @lc app=leetcode id=3695 lang=java
//
// [3695] Maximize Alternating Sum Using Swaps
//
// @lc code=start
import java.util.*;
class Solution {
    private int[] parent;
    private int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
    private void union(int x, int y) {
        parent[find(x)] = find(y);
    }
    public long maxAlternatingSum(int[] nums, int[][] swaps) {
        int n = nums.length;
        parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        for (int[] swap : swaps) union(swap[0], swap[1]);
        Map<Integer, List<Integer>> groups = new HashMap<>();
        for (int i = 0; i < n; i++) {
            int root = find(i);
            groups.computeIfAbsent(root, k -> new ArrayList<>()).add(i);
        }
        int[] arranged = new int[n];
        for (List<Integer> idxs : groups.values()) {
            List<Integer> evenIdx = new ArrayList<>();
            List<Integer> oddIdx = new ArrayList<>();
            List<Integer> vals = new ArrayList<>();
            for (int idx : idxs) {
                vals.add(nums[idx]);
                if (idx % 2 == 0) evenIdx.add(idx);
                else oddIdx.add(idx);
            }
            Collections.sort(vals, Collections.reverseOrder());
            // Assign largest to even, smallest to odd
            int ptr = 0;
            Collections.sort(evenIdx);
            Collections.sort(oddIdx);
            for (int idx : evenIdx) arranged[idx] = vals.get(ptr++);
            for (int idx : oddIdx) arranged[idx] = vals.get(vals.size() - (oddIdx.size() - oddIdx.indexOf(idx)));
            // Verification step (general):
            // For each assigned value, confirm it is paired with the index (even/odd) that maximizes its weighted contribution.
        }
        long sum = 0;
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0) sum += arranged[i];
            else sum -= arranged[i];
        }
        return sum;
    }
}
// @lc code=end