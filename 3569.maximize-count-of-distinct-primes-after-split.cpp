#
# @lc app=leetcode id=3569 lang=cpp
#
# [3569] Maximize Count of Distinct Primes After Split
#
# @lc code=start
class Solution {
public:
    vector<int> maximumCount(vector<int>& nums, vector<vector<int>>& queries) {
        // Initialize a prime sieve to determine primes up to 100000
        const int MAX_VAL = 100000;
        vector<bool> isPrime(MAX_VAL + 1, true);
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i * i <= MAX_VAL; ++i) {
            if (isPrime[i]) {
                for (int j = i * i; j <= MAX_VAL; j += i) {
                    isPrime[j] = false;
                }
            }
        }
        
        auto getDistinctPrimeCount = [&](vector<int>& part) -> int {
            unordered_set<int> primesInPart;
            for (int num : part) {
                if (isPrime[num]) { primesInPart.insert(num); }
            }
            return primesInPart.size();
        };
        
        vector<int> results;
        for (auto& query : queries) {
            nums[query[0]] = query[1]; // Update nums according to the query.
            int maxDistinctPrimes = 0;
            for (int k = 1; k < nums.size(); ++k) { // Try every possible split. 
                vector<int> prefix(nums.begin(), nums.begin() + k); 
                vector<int> suffix(nums.begin() + k, nums.end()); 
                int currentPrimesCount = getDistinctPrimeCount(prefix) + getDistinctPrimeCount(suffix); 
                maxDistinctPrimes = max(maxDistinctPrimes, currentPrimesCount); 
            } 
            results.push_back(maxDistinctPrimes); 
        } 
        return results; 
    } 
}; 
# @lc code=end