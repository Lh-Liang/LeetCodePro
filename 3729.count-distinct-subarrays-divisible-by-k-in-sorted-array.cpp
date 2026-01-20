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
        long long distinct_good_count = 0;

        // Compress the array into runs of (value, count)
        vector<pair<int, int>> runs;
        if (n > 0) {
            int current_val = nums[0];
            int current_count = 1;
            for (int i = 1; i < n; ++i) {
                if (nums[i] == current_val) {
                    current_count++;
                } else {
                    runs.push_back({current_val, current_count});
                    current_val = nums[i];
                    current_count = 1;
                }
            }
            runs.push_back({current_val, current_count});
        }

        // Part 1: Subarrays consisting of a single distinct value (runs).
        // For a run of value V with length L, possible subarray lengths are 1 to L.
        // We need (len * V) % k == 0.
        for (auto& p : runs) {
            long long val = p.first;
            long long count = p.second;
            
            // We need to solve: (len * val) % k == 0 for 1 <= len <= count.
            // Let g = gcd(val, k). Then len * (val/g) % (k/g) == 0.
            // Since gcd(val/g, k/g) = 1, we must have len % (k/g) == 0.
            // Let step = k / gcd(val, k).
            // Valid lengths are step, 2*step, 3*step, ... <= count.
            // Number of such lengths = floor(count / step).
            
            long long step = k / std::gcd((long long)k, val);
            if (step <= count) {
                distinct_good_count += (count / step);
            }
        }

        // Part 2: Subarrays containing at least two distinct values.
        // These subarrays span across multiple runs. 
        // A subarray starts inside run `i` (taking suffix of run `i`) 
        // and ends inside run `j` (taking prefix of run `j`) where i < j.
        // Unlike Part 1, every such valid subarray is unique because the sequence of values is unique.
        
        // Let the runs be R_0, R_1, ..., R_m.
        // A subarray spanning from R_start to R_end (start < end) looks like:
        // Suffix of R_start + Full R_{start+1} ... R_{end-1} + Prefix of R_end.
        // Let suffix length of R_start be `a` (1 <= a <= runs[start].count).
        // Let prefix length of R_end be `b` (1 <= b <= runs[end].count).
        // Sum = (a * val_start) + (Sum of full runs in between) + (b * val_end).
        // Sum = (a * val_start) + PrefixSumRuns[end] - PrefixSumRuns[start+1] + (b * val_end).
        // We need Sum % k == 0.
        // Rearranging: 
        // a * val_start + b * val_end + (BlockSum) == 0 (mod k)
        // a * val_start + b * val_end == -BlockSum (mod k)
        // Let Target = (-BlockSum % k + k) % k.
        // We need to count pairs (a, b) such that:
        // (a * val_start + b * val_end) % k == Target
        // where 1 <= a <= Count_start, 1 <= b <= Count_end.

        // We can iterate over all pairs of runs (start, end). Since N <= 10^5, number of runs can be up to N.
        // O(Runs^2) is too slow if many short runs. However, if runs are long, Runs count is small.
        // Actually, we can fix `start` and iterate `end`. 
        // Or even better, iterate `end` and maintain information about all previous `start`s.
        
        // Let's rewrite the condition:
        // (a * val_start - PrefixSumRuns[start+1]) + (b * val_end + PrefixSumRuns[end]) == 0 (mod k).
        // Let term_start(a) = (a * val_start - PrefixSumRuns[start+1]) % k.
        // Let term_end(b) = (b * val_end + PrefixSumRuns[end]) % k.
        // We need term_start(a) + term_end(b) == 0 (mod k).
        // i.e., term_start(a) == -term_end(b) (mod k).
        
        // As we iterate `end` from 1 to m, we want to count matches with all `start < end`.
        // We can maintain a frequency map of all valid `term_start(a)` values for all previous runs.
        // For the current run `end` (now treating it as the closing run), we calculate `term_end(b)` for all 1 <= b <= count.
        // Then we look up the complement in the map.
        // After processing run `end` as a closing run, we must add its contributions as a starting run for future runs.
        
        // Optimization: `term_start(a)` corresponds to `(a * val - NextPrefixSum) % k`.
        // Notice that `a` ranges from 1 to Count. The values `a * val % k` form an arithmetic progression modulo k.
        // Instead of adding `Count` entries to a hash map (which could be O(N) total per run, leading to O(N^2) worst case),
        // we need to handle the updates and queries efficiently. 
        // Wait, constraints are N=10^5, K=10^9. We cannot use an array of size K.
        // The number of distinct values in the map is at most N.
        
        // Let's check the update size. For a run of length L, we add L entries. Total L over all runs is N.
        // So total updates to the map is N. Total queries is also N.
        // Using a hash map (unordered_map or simpler custom hash), complexity is O(N).
        // Prefix sums of full runs:
        int m = runs.size();
        vector<long long> run_full_sum(m, 0);
        for(int i=0; i<m; ++i) {
            run_full_sum[i] = (1LL * runs[i].first * runs[i].second) % k;
        }
        
        vector<long long> prefix_run_sum(m + 1, 0);
        for(int i=0; i<m; ++i) {
            prefix_run_sum[i+1] = (prefix_run_sum[i] + run_full_sum[i]) % k;
        }

        // Map stores count of remainders: remainder -> count
        unordered_map<int, int> remainder_counts;

        for (int i = 0; i < m; ++i) {
            long long val = runs[i].first;
            long long count = runs[i].second;

            // 1. Query: Treat current run `i` as the END of a multi-run subarray.
            // We iterate b from 1 to count.
            // term_end(b) = (b * val + prefix_run_sum[i]) % k.
            // We need count of term_start such that term_start == (-term_end(b)) % k.
            // Target remainder R = (k - term_end(b) % k) % k.
            
            // This loop runs `count` times. Sum of `count` is N. So this part is O(N).
            for (int b = 1; b <= count; ++b) {
                long long current_rem = (b * val + prefix_run_sum[i]) % k;
                long long target = (k - current_rem) % k;
                if (remainder_counts.count(target)) {
                    distinct_good_count += remainder_counts[target];
                }
            }

            // 2. Update: Treat current run `i` as the START of a multi-run subarray.
            // We iterate a from 1 to count.
            // term_start(a) = (a * val - prefix_run_sum[i+1]) % k.
            // Add these to the map.
            for (int a = 1; a <= count; ++a) {
                long long rem = (a * val - prefix_run_sum[i+1]) % k;
                if (rem < 0) rem += k;
                remainder_counts[rem]++;
            }
        }

        return distinct_good_count;
    }
};
# @lc code=end