#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    long long maxSumTrionic(vector<int>& nums) {
        int n = nums.size();
        const long long INF = 1e18;

        // max_inc_prefix[p]: Max sum of strictly increasing nums[l...p] with l < p
        vector<long long> max_inc_prefix(n, -INF);
        for (int i = 1; i < n; ++i) {
            if (nums[i] > nums[i - 1]) {
                max_inc_prefix[i] = (long long)nums[i] + max((long long)nums[i - 1], max_inc_prefix[i - 1]);
            }
        }

        // max_inc_suffix[q]: Max sum of strictly increasing nums[q...r] with q < r
        vector<long long> max_inc_suffix(n, -INF);
        for (int i = n - 2; i >= 0; --i) {
            if (nums[i] < nums[i + 1]) {
                max_inc_suffix[i] = (long long)nums[i] + max((long long)nums[i + 1], max_inc_suffix[i + 1]);
            }
        }

        // Prefix sums for range sum calculation
        vector<long long> pref(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            pref[i + 1] = pref[i] + nums[i];
        }

        long long max_trionic_sum = -INF;
        // best_peak_contribution stores the max value of [Sum(l, p) - pref[p+1]]
        // for a peak p that is part of a strictly decreasing sequence ending at current q
        long long best_peak_contribution = -INF;

        // We need l < p < q < r. 
        // Smallest possible p is 1 (l=0). Smallest possible q is 2 (p=1).
        // Largest possible q is n-2 (r=n-1).
        for (int q = 2; q <= n - 2; ++q) {
            // Can we extend the decreasing sequence from q-1 to q?
            if (nums[q] < nums[q - 1]) {
                // The previous index q-1 is a potential peak p
                if (max_inc_prefix[q - 1] != -INF) {
                    best_peak_contribution = max(best_peak_contribution, max_inc_prefix[q - 1] - pref[q]);
                }
            } else {
                // Decreasing sequence broken
                best_peak_contribution = -INF;
            }

            // If we have a valid peak-to-valley path and a valid suffix increasing path
            if (best_peak_contribution != -INF && max_inc_suffix[q] != -INF) {
                // Formula: (Sum(l, p) - pref[p+1]) + pref[q] + Sum(q, r)
                max_trionic_sum = max(max_trionic_sum, best_peak_contribution + pref[q] + max_inc_suffix[q]);
            }
        }

        return max_trionic_sum;
    }
};