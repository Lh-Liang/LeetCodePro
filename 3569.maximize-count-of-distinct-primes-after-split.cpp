#
# @lc app=leetcode id=3569 lang=cpp
#
# [3569] Maximize Count of Distinct Primes After Split
#
# @lc code=start
class Solution {
public:
    vector<bool> isPrime;
    
    void sieve(int maxVal) {
        isPrime.assign(maxVal + 1, true);
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i * i <= maxVal; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= maxVal; j += i) {
                    isPrime[j] = false;
                }
            }
        }
    }
    
    vector<int> maximumCount(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        sieve(100000);
        
        vector<int> result;
        
        for (auto& query : queries) {
            int idx = query[0];
            int val = query[1];
            nums[idx] = val;
            
            // Compute prefix distinct prime counts
            vector<int> prefixCount(n);
            unordered_set<int> primes;
            for (int i = 0; i < n; i++) {
                if (isPrime[nums[i]]) {
                    primes.insert(nums[i]);
                }
                prefixCount[i] = primes.size();
            }
            
            // Compute suffix distinct prime counts
            vector<int> suffixCount(n);
            primes.clear();
            for (int i = n - 1; i >= 0; i--) {
                if (isPrime[nums[i]]) {
                    primes.insert(nums[i]);
                }
                suffixCount[i] = primes.size();
            }
            
            int maxCount = 0;
            // Try each split position k (1 <= k < n)
            for (int k = 1; k < n; k++) {
                // Prefix is [0..k-1], suffix is [k..n-1]
                int count = prefixCount[k - 1] + suffixCount[k];
                maxCount = max(maxCount, count);
            }
            
            result.push_back(maxCount);
        }
        
        return result;
    }
};
# @lc code=end