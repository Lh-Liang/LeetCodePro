#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

class Solution {
public:
    int minStable(vector<int>& nums, int maxC) {
        int n = nums.size();
        if (maxC >= n) return 0;

        // Pre-calculate primes up to sqrt(10^9)
        const int MAX_SQRT = 31622;
        static vector<int> primes;
        if (primes.empty()) {
            vector<bool> is_prime(MAX_SQRT + 1, true);
            is_prime[0] = is_prime[1] = false;
            for (int p = 2; p * p <= MAX_SQRT; p++) {
                if (is_prime[p]) {
                    for (int i = p * p; i <= MAX_SQRT; i += p)
                        is_prime[i] = false;
                }
            }
            for (int p = 2; p <= MAX_SQRT; p++) {
                if (is_prime[p]) primes.push_back(p);
            }
        }

        // Collect (prime, index) pairs
        vector<pair<int, int>> prime_index;
        for (int i = 0; i < n; ++i) {
            int x = nums[i];
            if (x < 2) continue;
            for (int p : primes) {
                if (p * p > x) break;
                if (x % p == 0) {
                    prime_index.push_back({p, i});
                    while (x % p == 0) x /= p;
                }
            }
            if (x > 1) prime_index.push_back({x, i});
        }

        // Sort and find maximal segments for each prime
        sort(prime_index.begin(), prime_index.end());
        vector<pair<int, int>> all_segments;
        int m = prime_index.size();
        for (int i = 0; i < m; ) {
            int j = i;
            int start = prime_index[i].second;
            int last = start;
            while (j + 1 < m && prime_index[j+1].first == prime_index[i].first) {
                if (prime_index[j+1].second == last + 1) {
                    last++;
                    j++;
                } else {
                    all_segments.push_back({start, last});
                    j++;
                    start = prime_index[j].second;
                    last = start;
                }
            }
            all_segments.push_back({start, last});
            i = j + 1;
        }

        // Sort all segments by start point for efficient merging
        sort(all_segments.begin(), all_segments.end());

        auto check = [&](int L) {
            if (L == n) return true;
            long long count = 0;
            int current_S = -1, current_E = -1;
            for (const auto& seg : all_segments) {
                if (seg.second - seg.first + 1 > L) {
                    int S = seg.first + L;
                    int E = seg.second;
                    if (S > current_E) {
                        if (current_S != -1) {
                            count += (current_E - current_S) / (L + 1) + 1;
                        }
                        current_S = S;
                        current_E = E;
                    } else {
                        current_E = max(current_E, E);
                    }
                }
            }
            if (current_S != -1) {
                count += (current_E - current_S) / (L + 1) + 1;
            }
            return count <= (long long)maxC;
        };

        int low = 0, high = n;
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (check(mid)) high = mid;
            else low = mid + 1;
        }

        return low;
    }
};