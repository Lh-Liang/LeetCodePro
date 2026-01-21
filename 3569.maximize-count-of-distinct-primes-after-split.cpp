#
# @lc app=leetcode id=3569 lang=cpp
#
# [3569] Maximize Count of Distinct Primes After Split
#
# @lc code=start
class Solution {
public:
    vector<bool> sieve(int maxVal) {
        vector<bool> isPrime(maxVal + 1, true);
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i * i <= maxVal; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= maxVal; j += i) {
                    isPrime[j] = false;
                }
            }
        }
        return isPrime;
    }
    
    vector<int> maximumCount(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        vector<bool> isPrime = sieve(100000);
        vector<int> result;
        
        for (const auto& query : queries) {
            int idx = query[0];
            int val = query[1];
            nums[idx] = val;
            
            vector<int> prefixCount(n);
            unordered_set<int> currentSet;
            for (int i = 0; i < n; i++) {
                if (isPrime[nums[i]]) {
                    currentSet.insert(nums[i]);
                }
                prefixCount[i] = currentSet.size();
            }
            
            vector<int> suffixCount(n);
            currentSet.clear();
            for (int i = n - 1; i >= 0; i--) {
                if (isPrime[nums[i]]) {
                    currentSet.insert(nums[i]);
                }
                suffixCount[i] = currentSet.size();
            }
            
            int maxCount = 0;
            for (int k = 1; k < n; k++) {
                int count = prefixCount[k-1] + suffixCount[k];
                maxCount = max(maxCount, count);
            }
            
            result.push_back(maxCount);
        }
        
        return result;
    }
};
# @lc code=end