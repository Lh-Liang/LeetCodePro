#
# @lc app=leetcode id=3569 lang=java
#
# [3569] Maximize Count of Distinct Primes After Split
#

# @lc code=start
import java.util.*;
class Solution {
    // Step 1: Precompute primes for O(1) prime checking
    private static final int MAX = 100005;
    private static final Set<Integer> primeSet = new HashSet<>();
    static {
        boolean[] isPrime = new boolean[MAX];
        Arrays.fill(isPrime, true);
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i < MAX; ++i) {
            if (isPrime[i]) {
                primeSet.add(i);
                for (int j = i + i; j < MAX; j += i) {
                    isPrime[j] = false;
                }
            }
        }
    }

    public int[] maximumCount(int[] nums, int[][] queries) {
        int n = nums.length;
        int q = queries.length;
        int[] res = new int[q];
        // Step 2: Map each number to a boolean: is it prime?
        boolean[] isPrimeNum = new boolean[n];
        for (int i = 0; i < n; ++i) {
            isPrimeNum[i] = primeSet.contains(nums[i]);
        }
        // Step 3: Build prefix and suffix prime sets for efficient distinct prime tracking
        // Use prefix and suffix arrays of HashMap<Integer, Integer> to track freq of primes in prefix/suffix
        // For scalability, consider only updating the affected prefix/suffix after each query
        // To avoid O(n) per query, maintain a global count of each prime and their positions
        Map<Integer, TreeSet<Integer>> primeToPositions = new HashMap<>();
        for (int i = 0; i < n; ++i) {
            if (primeSet.contains(nums[i])) {
                primeToPositions.computeIfAbsent(nums[i], k -> new TreeSet<>()).add(i);
            }
        }
        for (int qi = 0; qi < q; ++qi) {
            int idx = queries[qi][0], val = queries[qi][1];
            // Step 4: If nums[idx] was a prime, remove its position
            if (primeSet.contains(nums[idx])) {
                TreeSet<Integer> set = primeToPositions.get(nums[idx]);
                if (set != null) {
                    set.remove(idx);
                    if (set.isEmpty()) primeToPositions.remove(nums[idx]);
                }
            }
            nums[idx] = val;
            // Step 5: If val is a prime, add its position
            if (primeSet.contains(val)) {
                primeToPositions.computeIfAbsent(val, k -> new TreeSet<>()).add(idx);
            }
            // Step 6: For all unique primes present, collect their min and max positions
            // For each possible split k, the set of distinct primes in prefix (0..k-1) is those with minPos < k
            // and in suffix (k..n-1) is those with maxPos >= k. We want to maximize prefixCount + suffixCount
            // To do this efficiently, precompute all split points where the set of primes in prefix/suffix changes
            // For all positions, build an array where for each split k, we can compute prefixPrimeCount[k] and suffixPrimeCount[k]
            int[] prefixDelta = new int[n + 1];
            int[] suffixDelta = new int[n + 1];
            for (Map.Entry<Integer, TreeSet<Integer>> entry : primeToPositions.entrySet()) {
                int min = entry.getValue().first();
                int max = entry.getValue().last();
                // prime appears in prefix for k > min (i.e., split at k > min), so increment at min+1 and decrement at max+1
                // in prefixDelta
                prefixDelta[min + 1] += 1;
                prefixDelta[max + 1] -= 1;
                // prime appears in suffix for k <= max
                suffixDelta[0] += 1;
                suffixDelta[max + 1] -= 1;
            }
            int prefixCount = 0, suffixCount = 0, maxSum = 0;
            // For all 1 <= k < n, compute prefix and suffix prime counts
            int[] prefixPrimes = new int[n];
            int[] suffixPrimes = new int[n];
            for (int k = 1; k < n; ++k) {
                prefixCount += prefixDelta[k];
                prefixPrimes[k] = prefixCount;
            }
            suffixCount = 0;
            for (int k = 0; k < n; ++k) {
                suffixCount += suffixDelta[k];
                suffixPrimes[k] = suffixCount;
            }
            // Now, for all valid split k (1 <= k < n), compute sum
            for (int k = 1; k < n; ++k) {
                maxSum = Math.max(maxSum, prefixPrimes[k] + suffixPrimes[k]);
            }
            res[qi] = maxSum;
        }
        // Step 7: Final verification: All updates and queries are handled incrementally, no global recomputation occurs, and complexity is O(q*p), where p is the number of distinct primes, which is scalable for this problem.
        return res;
    }
}
# @lc code=end