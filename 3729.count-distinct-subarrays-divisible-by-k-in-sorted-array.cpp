#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    long long numGoodSubarrays(vector<int>& nums, int k) {
        int n = (int)nums.size();
        // Compress into runs
        vector<long long> vals;
        vector<int> cnt;
        vals.reserve(n);
        cnt.reserve(n);
        for (int i = 0; i < n; ) {
            int j = i;
            while (j < n && nums[j] == nums[i]) j++;
            vals.push_back(nums[i]);
            cnt.push_back(j - i);
            i = j;
        }

        unordered_map<long long, long long> freq;
        freq.reserve((size_t)n * 2);
        freq.max_load_factor(0.7f);

        long long ans = 0;
        long long prefixMod = 0; // sum of all previous runs modulo k

        for (int idx = 0; idx < (int)vals.size(); idx++) {
            long long v = vals[idx];
            int c = cnt[idx];

            // 1) within-run distinct good subarrays (lengths only)
            long long g = std::gcd((long long)k, v);
            long long d = (long long)k / g; // t must be multiple of d
            ans += (long long)c / d;

            // If k==1, v%k==0; in general keep vmod
            long long vmod = v % k;

            // 2) count multi-run subarrays ending in this run
            // end residues for t = 1..c
            for (int t = 1; t <= c; t++) {
                long long r = (prefixMod + ( (__int128)t * vmod) % k) % k;
                auto it = freq.find(r);
                if (it != freq.end()) ans += it->second;
            }

            // 3) add start residues from this run for future runs
            // start residues correspond to x=0..c-1 (exclude boundary after the run)
            for (int x = 0; x <= c - 1; x++) {
                long long r = (prefixMod + ( (__int128)x * vmod) % k) % k;
                freq[r] += 1;
            }

            // 4) advance prefixMod by full run sum
            prefixMod = (prefixMod + ( (__int128)c * vmod) % k) % k;
        }

        return ans;
    }
};
// @lc code=end
