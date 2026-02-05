#
# @lc app=leetcode id=3695 lang=java
#
# [3695] Maximize Alternating Sum Using Swaps
#

# @lc code=start
class Solution {
    public long maxAlternatingSum(int[] nums, int[][] swaps) {
        int n = nums.length;
        DSU dsu = new DSU(n);
        
        // Process swap operations to form connected components
        for (int[] swap : swaps) {
            dsu.union(swap[0], swap[1]);
        }
        
        // Create a map of components and their respective indices in nums
        Map<Integer, List<Integer>> components = new HashMap<>();
        for (int i = 0; i < n; i++) {
            int root = dsu.find(i);
            components.computeIfAbsent(root, k -> new ArrayList<>()).add(i);
        }
        
        long maxSum = 0;
        // Iterate over each component, sort it, and calculate its contribution to max alternating sum
        for (List<Integer> indices : components.values()) {
            List<Integer> values = new ArrayList<>();
            for (int index : indices) {
                values.add(nums[index]);
            }
            Collections.sort(values, Collections.reverseOrder()); // Sort descending for max alternation benefit
            
            // Calculate alternating sum contribution of this component's sorted values list
            long localSum = 0;
            for (int i = 0; i < values.size(); i++) {
                if (i % 2 == 0) { // Even index in our local array contributes positively to the sum.
                    localSum += values.get(i);
                } else { // Odd index contributes negatively.                    localSum -= values.get(i);                }            }            maxSum += localSum;        }       return maxSum;   }}// Definition of DSU class:class DSU {    private int[] parent;    public DSU(int size) {        parent = new int[size];        for (int i = 0; i < size; i++) {            parent[i] = i;        }    }    public int find(int x) {        if (parent[x] != x) {            parent[x] = find(parent[x]); // Path compression        }        return parent[x];    }    public void union(int x, int y) {        int rootX = find(x);        int rootY = find(y);        if (rootX != rootY) {            parent[rootX] = rootY; // Union by rank could be added here        }    }}# @lc code=end