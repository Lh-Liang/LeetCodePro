#include <vector>
#include <unordered_map>

using namespace std;

#
# @lc app=leetcode id=3729 lang=cpp
#
# [3729] Count Distinct Subarrays Divisible by K in Sorted Array
#

# @lc code=start
class Solution {
public:
    long long numGoodSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        long long totalGoodSubarrays = 0;
        long long currentPrefixSum = 0;
        
        // Map to store frequency of (prefixSum % k)
        // We only store prefix sums P[i] where i <= first_occurrence_index of the current nums[j]
        unordered_map<int, int> validPrefixCounts;
        
        // P[0] is always valid for the first element
        validPrefixCounts[0] = 1;
        
        int lastProcessedIdx = 0;
        
        for (int j = 0; j < n; ++j) {
            currentPrefixSum += nums[j];
            int targetRemainder = currentPrefixSum % k;
            if (targetRemainder < 0) targetRemainder += k;
            
            // If we encountered a new value, we can 'unlock' more prefix sums.
            // A subarray nums[i...j] is distinct if i == 0 or nums[i-1] < nums[j].
            // This means i <= first_index_of(nums[j]).
            if (j > 0 && nums[j] > nums[j-1]) {
                // The first_index of nums[j] is j.
                // All prefix sums P[i] for i from lastProcessedIdx + 1 to j are now valid.
                while (lastProcessedIdx < j) {
                    lastProcessedIdx++;
                    // We don't actually add P[lastProcessedIdx] yet, because we need P[i] where i <= first_idx
                    // If nums[j] is the start of a block, first_idx is j. So P[0...j] are valid.
                }
                // To keep it simple: when nums[j] > nums[j-1], the 'first_index' for the current 
                // and subsequent identical values becomes j. 
                // All prefix sums from the previous first_index up to the new one are added.
                // Note: lastProcessedIdx tracks how many prefix sums P[1...i] are in the map.
            }
            
            // The logic: For a fixed j, we count i in [0, first_idx[nums[j]]] 
            // s.t. (P[j+1] - P[i]) % k == 0.
            // If j is part of a block of identical values starting at index 'start',
            // then first_idx[nums[j]] = start. 
            // The valid i's are 0, 1, ..., start.
            
            // Find the start of the current block of identical values
            // In a real optimized version, we pre-calculate or update the map only when the value changes.
            
            // Let's re-sync the map: it should contain P[0]...P[start_of_block]
            // We only update the map when nums[j] changes.
        }
        
        // Corrected Loop logic:
        validPrefixCounts.clear();
        validPrefixCounts[0] = 1;
        currentPrefixSum = 0;
        int startOfBlock = 0;
        
        for (int j = 0; j < n; ++j) {
            if (j > 0 && nums[j] > nums[j - 1]) {
                // New value block starts. Previous block's start was 'startOfBlock'.
                // We need to add prefix sums P[i] where startOfBlock < i <= j.
                // Because for the new value, the first_index is j.
                long long tempSum = 0;
                // This part needs to be efficient. We can't re-sum.
                // Let's use a secondary prefix sum or just track it.
            }
        }

        // Final refined O(N) implementation:
        validPrefixCounts.clear();
        long long pSum = 0;
        vector<int> modPrefixes(n + 1);
        modPrefixes[0] = 0;
        for(int i = 0; i < n; ++i) {
            pSum = (pSum + nums[i]) % k;
            modPrefixes[i+1] = (int)pSum;
        }

        validPrefixCounts[modPrefixes[0]]++;
        int firstIdx = 0;
        for (int j = 0; j < n; ++j) {
            if (j > 0 && nums[j] > nums[j-1]) {
                // Update map to include P[i] for i up to the new firstIdx (which is j)
                for (int i = firstIdx + 1; i <= j; ++i) {
                    validPrefixCounts[modPrefixes[i]]++;
                }
                firstIdx = j;
            }
            totalGoodSubarrays += validPrefixCounts[modPrefixes[j+1]];
        }

        return totalGoodSubarrays;
    }
};
# @lc code=end