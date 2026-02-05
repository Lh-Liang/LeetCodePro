# @lc app=leetcode id=3762 lang=java
# [3762] Minimum Operations to Equalize Subarrays
# @lc code=start
class Solution {
    public long[] minOperations(int[] nums, int k, int[][] queries) {
        int qLen = queries.length;
        long[] result = new long[qLen];
        for (int qi = 0; qi < qLen; qi++) {
            int li = queries[qi][0];
            int ri = queries[qi][1];
            List<Integer> subArray = new ArrayList<>();
            boolean possible = true;
            for (int i = li; i <= ri; i++) {
                subArray.add(nums[i]);
            }
            Collections.sort(subArray);
            // Check feasibility
            for (int i = 1; i < subArray.size(); i++) {
                if ((subArray.get(i) - subArray.get(0)) % k != 0) {
                    possible = false;
                    break;
                }
            }
            if (!possible) {
                result[qi] = -1;
                continue;
            }
            // Calculate minimum operations using sorted array and prefix sums
            int n = subArray.size();
            long[] prefixSum = new long[n+1];
            for (int i = 0; i < n; i++) {
                prefixSum[i+1] = prefixSum[i] + subArray.get(i);
            }
            long minOps = Long.MAX_VALUE;
            for (int i = 0; i < n; i++) {
                long opsToLeft = (long)i * subArray.get(i) - prefixSum[i];
                long opsToRight = (prefixSum[n] - prefixSum[i+1]) - (long)(n-i-1) * subArray.get(i);
                minOps = Math.min(minOps, (opsToLeft + opsToRight) / k);
            }
            result[qi] = minOps;
        }
        return result;
    }
}
# @lc code=end