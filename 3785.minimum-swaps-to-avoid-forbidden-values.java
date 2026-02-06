#
# @lc app=leetcode id=3785 lang=java
#
# [3785] Minimum Swaps to Avoid Forbidden Values
#

# @lc code=start
class Solution {
    public int minSwaps(int[] nums, int[] forbidden) {
        int n = nums.length;
        int[] pos = new int[n];
        for (int i = 0; i < n; ++i) pos[i] = i;
        boolean[] visited = new boolean[n];
        int swaps = 0;

        // Build mapping from value to indices (positions)
        Map<Integer, List<Integer>> valToIdx = new HashMap<>();
        for (int i = 0; i < n; ++i) {
            valToIdx.computeIfAbsent(nums[i], k -> new ArrayList<>()).add(i);
        }
        // To find a derangement avoiding forbidden[i], we need to try to permute nums such that nums[i] != forbidden[i] for all i
        // This can be solved by finding cycles in the initial permutation and checking for forbidden constraints
        int[] target = new int[n];
        Arrays.fill(target, -1);
        boolean possible = true;
        // For each index, try to assign a value that is not forbidden[i], and try to keep original positions if possible
        Map<Integer, Integer> count = new HashMap<>();
        for (int num : nums) count.put(num, count.getOrDefault(num,0)+1);
        List<Integer> available = new ArrayList<>();
        for (int num : nums) available.add(num);
        // Try to create a derangement avoiding forbidden[i] for each i
        for (int i = 0; i < n; ++i) {
            boolean found = false;
            for (int j = 0; j < available.size(); ++j) {
                int cand = available.get(j);
                if (cand != forbidden[i] && !(cand == nums[i] && forbidden[i] == nums[i] && count.get(nums[i]) == 1)) {
                    target[i] = cand;
                    available.remove(j);
                    found = true;
                    break;
                }
            }
            if (!found) {
                possible = false;
                break;
            }
        }
        if (!possible) return -1;
        // Now, count minimum swaps to convert nums to target
        Map<Integer, Queue<Integer>> valToQueue = new HashMap<>();
        for (int i = 0; i < n; ++i) {
            valToQueue.computeIfAbsent(target[i], k -> new LinkedList<>()).add(i);
        }
        int[] perm = new int[n];
        for (int i = 0; i < n; ++i) {
            perm[i] = valToQueue.get(nums[i]).poll();
        }
        boolean[] done = new boolean[n];
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            if (done[i] || perm[i] == i) continue;
            int cycle = 0;
            int j = i;
            while (!done[j]) {
                done[j] = true;
                j = perm[j];
                cycle++;
            }
            ans += cycle - 1;
        }
        return ans;
    }
}
# @lc code=end