#
# @lc app=leetcode id=3670 lang=java
#
# [3670] Maximum Product of Two Integers With No Common Bits
#
# @lc code=start
class Solution {
    public long maxProduct(int[] nums) {
        // Map from bitmask to a list of (value, index) pairs
        Map<Integer, List<int[]>> maskToVals = new HashMap<>();
        for (int i = 0; i < nums.length; ++i) {
            int mask = nums[i];
            maskToVals.putIfAbsent(mask, new ArrayList<>());
            maskToVals.get(mask).add(new int[]{nums[i], i});
        }
        // For each mask, keep top 2 largest (value, index) pairs
        Map<Integer, List<int[]>> top2ForMask = new HashMap<>();
        for (Map.Entry<Integer, List<int[]>> entry : maskToVals.entrySet()) {
            List<int[]> list = entry.getValue();
            list.sort((a, b) -> b[0] - a[0]);
            List<int[]> top2 = new ArrayList<>();
            for (int j = 0; j < Math.min(2, list.size()); ++j) top2.add(list.get(j));
            top2ForMask.put(entry.getKey(), top2);
        }
        long res = 0;
        List<Integer> masks = new ArrayList<>(top2ForMask.keySet());
        int m = masks.size();
        for (int i = 0; i < m; ++i) {
            int mask1 = masks.get(i);
            List<int[]> l1 = top2ForMask.get(mask1);
            for (int j = i; j < m; ++j) {
                int mask2 = masks.get(j);
                if ((mask1 & mask2) == 0) {
                    List<int[]> l2 = top2ForMask.get(mask2);
                    if (i == j && l1.size() >= 2) {
                        int[] a = l1.get(0), b = l1.get(1);
                        if (a[1] != b[1]) res = Math.max(res, 1L * a[0] * b[0]);
                    } else if (i != j) {
                        int[] a = l1.get(0), b = l2.get(0);
                        if (a[1] != b[1]) res = Math.max(res, 1L * a[0] * b[0]);
                    }
                }
            }
        }
        return res;
    }
}
# @lc code=end