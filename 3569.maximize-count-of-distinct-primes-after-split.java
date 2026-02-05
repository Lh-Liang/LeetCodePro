#
# @lc app=leetcode id=3569 lang=java
#
# [3569] Maximize Count of Distinct Primes After Split
#

# @lc code=start
class Solution {
    private boolean[] isPrime;
    
    public Solution() {
        // Precompute prime numbers using Sieve of Eratosthenes
        isPrime = new boolean[100001];
        Arrays.fill(isPrime, true);
        isPrime[0] = false;
        isPrime[1] = false;
        for (int i = 2; i * i < isPrime.length; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j < isPrime.length; j += i) {
                    isPrime[j] = false;
                }
            }
        }
    }
    
    public int[] maximumCount(int[] nums, int[][] queries) {
        int n = nums.length;
        int[] results = new int[queries.length];

        // Initialize prefix and suffix arrays for distinct prime counts
        int[] prefixPrimes = new int[n+1];
        int[] suffixPrimes = new int[n+1];

        // Helper function to update arrays with distinct prime counts efficiently
        updatePrimes(nums, prefixPrimes, suffixPrimes);

        // Process queries
        for (int q = 0; q < queries.length; q++) {		// Efficiently update affected segments based on changes.	int idx = queries[q][0]; 	int val = queries[q][1]; 	nums[idx] = val;	updatePrimes(nums, prefixPrimes, suffixPrimes);	// Compute maximum sum of distinct primes for current configuration	int maxPrimeCount = 0;	for (int k = 1; k < n; k++) {maxPrimeCount = Math.max(maxPrimeCount, prefixPrimes[k] + suffixPrimes[k]);}results[q] = maxPrimeCount;}return results;}private void updatePrimes(int[] nums, int[] prefixPrimes, int[] suffixPrimes) {Set<Integer> seenPrimesPrefix = new HashSet<>();Set<Integer> seenPrimesSuffix = new HashSet<>();// Update prefix primesfor (int i = 0; i < nums.length; i++) {if (isPrime[nums[i]]) seenPrimesPrefix.add(nums[i]);prefixPrimes[i + 1] = seenPrimesPrefix.size();}// Update suffix primesfrom endfor (int i = nums.length - 1; i >= 0; i--) {if (isPrime[nums[i]]) seenPrimesSuffix.add(nums[i]);suffixPrimes[i] = seenPrimesSuffix.size();}} } # @lc code=end