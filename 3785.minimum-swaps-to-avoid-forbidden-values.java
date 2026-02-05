#
# @lc app=leetcode id=3785 lang=java
#
# [3785] Minimum Swaps to Avoid Forbidden Values
#
# @lc code=start
import java.util.*;
class Solution {
    public int minSwaps(int[] nums, int[] forbidden) {
        int n = nums.length;
        // Step 1: Trivial check
        boolean valid = true;
        for (int i = 0; i < n; ++i) {
            if (nums[i] == forbidden[i]) {
                valid = false;
                break;
            }
        }
        if (valid) return 0;
        // Step 2: Identify conflicts and build value-index maps
        List<Integer> conflicts = new ArrayList<>();
        Map<Integer, List<Integer>> valueToIndices = new HashMap<>();
        for (int i = 0; i < n; ++i) {
            valueToIndices.computeIfAbsent(nums[i], k -> new ArrayList<>()).add(i);
            if (nums[i] == forbidden[i]) conflicts.add(i);
        }
        // Step 3: Build position permutation for cycles
        int[] desired = new int[n];
        Arrays.fill(desired, -1);
        Map<Integer, Queue<Integer>> forbiddenMap = new HashMap<>();
        for (int i = 0; i < n; ++i) {
            forbiddenMap.computeIfAbsent(forbidden[i], k -> new LinkedList<>()).add(i);
        }
        // For each value, assign positions not forbidden
        boolean[] assigned = new boolean[n];
        for (int i = 0; i < n; ++i) {
            if (nums[i] == forbidden[i]) {
                // Try to find a position to move nums[i] to, such that it's not forbidden
                boolean found = false;
                List<Integer> candidates = valueToIndices.get(nums[i]);
                for (int idx : candidates) {
                    if (forbidden[idx] != nums[i] && !assigned[idx]) {
                        desired[i] = idx;
                        assigned[idx] = true;
                        found = true;
                        break;
                    }
                }
                if (!found) desired[i] = -1;
            }
        }
        // Step 4: Detect cycles and count swaps
        boolean[] visited = new boolean[n];
        int swaps = 0;
        for (int i : conflicts) {
            if (visited[i]) continue;
            // Trace cycle
            int len = 0;
            int curr = i;
            boolean validCycle = true;
            while (curr != -1 && !visited[curr]) {
                visited[curr] = true;
                len++;
                curr = desired[curr];
            }
            if (len > 1) {
                swaps += (len - 1);
            } else if (len == 1 && desired[i] == -1) {
                // No way to resolve this conflict
                return -1;
            }
        }
        // Step 5: Intermediate verification
        for (int i = 0; i < n; ++i) {
            if (nums[i] == forbidden[i]) return -1;
        }
        return swaps;
    }
}
# @lc code=end