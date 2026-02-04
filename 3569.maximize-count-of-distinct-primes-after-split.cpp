# @lc app=leetcode id=3569 lang=cpp
# [3569] Maximize Count of Distinct Primes After Split

# @lc code=start
class Solution {
public:
    vector<int> maximumCount(vector<int>& nums, vector<vector<int>>& queries) {
        int max_val = 100000; // Given constraint: max value in nums or queries is 10^5
        vector<bool> is_prime(max_val + 1, true);
        is_prime[0] = is_prime[1] = false;
        for (int i = 2; i * i <= max_val; ++i) {
            if (is_prime[i]) {
                for (int j = i * i; j <= max_val; j += i) {
                    is_prime[j] = false;
                }
            }
        }
        auto countDistinctPrimes = [&](const vector<int>& arr) -> int {
            unordered_set<int> prime_set;
            for (int num : arr) {
                if (is_prime[num]) {
                    prime_set.insert(num);
                }
            }
            return prime_set.size();
        };
        vector<int> results;
        for (auto& query : queries) {
            nums[query[0]] = query[1]; // Update nums with the current query.
            int n = nums.size();
            int max_distinct_primes = 0;
            unordered_set<int> prefix_primes, suffix_primes(nums.begin(), nums.end()); // Initialize suffix with all elements initially.
            int prefix_count = 0;
            int suffix_count = countDistinctPrimes(nums);
            for (int k = 1; k < n; ++k) { // Start from k=1 to ensure non-empty prefix and suffix
                if (is_prime[nums[k-1]]) {
prefix_primes.insert(nums[k-1]);
suffix_primes.erase(nums[k-1]);
prefix_count++; 
suffix_count--;
n}
nmax_distinct_primes = std::max(max_distinct_primes, prefix_count + suffix_count);
n}
nresults.push_back(max_distinct_primes);
n}
nreturn results;
n}
n};
n# @lc code=end