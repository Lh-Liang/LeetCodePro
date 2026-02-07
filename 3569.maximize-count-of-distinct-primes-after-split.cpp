#
# @lc app=leetcode id=3569 lang=cpp
#
# [3569] Maximize Count of Distinct Primes After Split
#

# @lc code=start
class Solution {
public:
    vector<int> sieve(int max_num) {
        vector<bool> is_prime(max_num + 1, true);
        is_prime[0] = is_prime[1] = false;
        for (int i = 2; i * i <= max_num; ++i) {
            if (is_prime[i]) {
                for (int j = i * i; j <= max_num; j += i) {
                    is_prime[j] = false;
                }
            }
        }
        vector<int> primes;
        for (int i = 2; i <= max_num; ++i) {
            if (is_prime[i]) primes.push_back(i);
        }
        return primes;
    }

    bool isPrime(int num, const unordered_set<int>& prime_set) {
        return prime_set.count(num) > 0;
    }
    
    vector<int> maximumCount(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        vector<int> results;
        vector<int> all_primes = sieve(100000);
        unordered_set<int> prime_set(all_primes.begin(), all_primes.end());

        for (const auto& query : queries) {
            int idx = query[0];
            int val = query[1];
            nums[idx] = val;

            vector<unordered_set<int>> prefix_primes(n), suffix_primes(n);
            unordered_set<int> seen_primes;

            // Build prefix primes count
            for (int i = 0; i < n; ++i) {
                if (isPrime(nums[i], prime_set)) seen_primes.insert(nums[i]);
                prefix_primes[i] = seen_primes;
            }

            seen_primes.clear();

            // Build suffix primes count
            for (int i = n - 1; i >= 0; --i) {
                if (isPrime(nums[i], prime_set)) seen_primes.insert(nums[i]);
                suffix_primes[i] = seen_primes;
            }

            int max_distinct_primes = 0;

            // Calculate max distinct primes between splits
            for (int k = 1; k < n; ++k) {
                int total_distinct_primes = prefix_primes[k-1].size() + suffix_primes[k].size();
                max_distinct_primes = max(max_distinct_primes, total_distinct_primes);
            }

            results.push_back(max_distinct_primes);
        }
        return results;
    }
};
# @lc code=end