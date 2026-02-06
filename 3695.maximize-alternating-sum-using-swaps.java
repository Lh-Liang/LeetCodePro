#
# @lc app=leetcode id=3695 lang=java
#
# [3695] Maximize Alternating Sum Using Swaps
#
# @lc code=start
import java.util.*;
class Solution {
    public long maxAlternatingSum(int[] nums, int[][] swaps) {
        int n = nums.length;
        DSU dsu = new DSU(n);
        for (int[] swap : swaps) {
            dsu.union(swap[0], swap[1]);
        }
        Map<Integer, List<Integer>> components = new HashMap<>();
        for (int i = 0; i < n; i++) {
            int root = dsu.find(i);
            components.computeIfAbsent(root, k -> new ArrayList<>()).add(i);
        }
        long res = 0;
        for (List<Integer> comp : components.values()) {
            List<Integer> vals = new ArrayList<>();
            for (int i : comp) vals.add(nums[i]);
            Collections.sort(vals, Collections.reverseOrder());
            Collections.sort(comp);
            for (int j = 0; j < comp.size(); j++) {
                if (comp.get(j) % 2 == 0) res += vals.get(j);
                else res -= vals.get(j);
            }
        }
        return res;
    }
}
class DSU {
    int[] parent;
    public DSU(int n) {
        parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;
    }
    public int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    public void union(int x, int y) {
        parent[find(x)] = find(y);
    }
}
# @lc code=end