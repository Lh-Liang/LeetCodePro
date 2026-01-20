#
# @lc app=leetcode id=3464 lang=cpp
#
# [3464] Maximize the Distance Between Points on a Square
#

# @lc code=start
class Solution {
public:
    int maxDistance(int side, vector<vector<int>>& points, int k) {
        long long S = side;
        vector<long long> t_vals;
        t_vals.reserve(points.size());

        // Lists for D > side case (k=4)
        // s0: Bottom (y=0), store x
        // s1: Right (x=side), store y
        // s2: Top (y=side), store x
        // s3: Left (x=0), store y
        vector<int> s0, s1, s2, s3;

        for (const auto& p : points) {
            int x = p[0];
            int y = p[1];
            
            // Map to 1D coordinate t
            long long t;
            if (y == 0) t = x;
            else if (x == side) t = S + y;
            else if (y == side) t = 2 * S + (S - x);
            else t = 3 * S + (S - y);
            t_vals.push_back(t);

            if (y == 0) s0.push_back(x);
            if (x == side) s1.push_back(y);
            if (y == side) s2.push_back(x);
            if (x == 0) s3.push_back(y);
        }

        sort(t_vals.begin(), t_vals.end());
        sort(s0.begin(), s0.end());
        sort(s1.begin(), s1.end());
        sort(s2.begin(), s2.end());
        sort(s3.begin(), s3.end());

        auto check = [&](long long D) -> bool {
            if (D <= S) {
                // Greedy circle check
                int n = t_vals.size();
                // We try to find a sequence of k points
                // Since the circle is symmetric, we can try starting from each point i.
                // However, we can just iterate i and greedily pick next points.
                // If we find any valid start, return true.
                
                // Optimization: We don't need to try all starts fully if we code carefully,
                // but O(N*K) is acceptable given constraints (N=15000, K=25).
                
                for (int i = 0; i < n; ++i) {
                    long long first_t = t_vals[i];
                    long long current_t = first_t;
                    int count = 1;
                    bool possible = true;
                    
                    // Greedily find next k-1 points
                    // To avoid O(N) scan for next point, we can use binary search or just linear scan pointer.
                    // Since we iterate i, linear scan is O(N) total (two pointers) if we just want *max* points,
                    // but here we need exactly k points with specific start.
                    // Binary search is O(K log N) per start. Total O(N K log N). A bit slow?
                    // 15000 * 25 * 14 ~ 5*10^6. That's fine.
                    
                    int curr_idx = i;
                    for (int step = 1; step < k; ++step) {
                        long long target = current_t + D;
                        auto it = lower_bound(t_vals.begin(), t_vals.end(), target);
                        if (it == t_vals.end()) {
                            possible = false;
                            break;
                        }
                        current_t = *it;
                        curr_idx = distance(t_vals.begin(), it);
                    }
                    
                    if (possible) {
                        // Check wraparound constraint
                        if (4 * S - (current_t - first_t) >= D) return true;
                    }
                }
                return false;
            } else {
                // Case D > S. Only possible if k <= 4.
                if (k > 4) return false;
                // For k=4, we need one point from each edge.
                if (s0.empty() || s1.empty() || s2.empty() || s3.empty()) return false;

                // Iterate x0 in s0
                for (int x0 : s0) {
                    long long min_y1 = x0 + D - S;
                    long long min_y3 = D - x0;

                    // Case A: y1 >= y3 + D - S
                    auto it_y3 = lower_bound(s3.begin(), s3.end(), min_y3);
                    if (it_y3 != s3.end()) {
                        int y3 = *it_y3;
                        long long req_y1 = max(min_y1, (long long)y3 + D - S);
                        auto it_y1 = lower_bound(s1.begin(), s1.end(), req_y1);
                        if (it_y1 != s1.end()) {
                            int y1 = *it_y1;
                            long long L = D - S + y3;
                            long long R = 2 * S - D - y1;
                            if (L <= R) {
                                // Check existence of x2 in [L, R] satisfying |x2 - x0| >= D - S
                                long long cut1 = x0 - (D - S);
                                long long cut2 = x0 + (D - S);
                                
                                // Check [L, R] intersect (-inf, cut1]
                                if (L <= cut1) {
                                    auto it = lower_bound(s2.begin(), s2.end(), L);
                                    if (it != s2.end() && *it <= min(R, cut1)) return true;
                                }
                                // Check [L, R] intersect [cut2, inf)
                                if (R >= cut2) {
                                    auto it = lower_bound(s2.begin(), s2.end(), max(L, cut2));
                                    if (it != s2.end() && *it <= R) return true;
                                }
                            }
                        }
                    }

                    // Case B: y3 >= y1 + D - S
                    auto it_y1_b = lower_bound(s1.begin(), s1.end(), min_y1);
                    if (it_y1_b != s1.end()) {
                        int y1 = *it_y1_b;
                        long long req_y3 = max(min_y3, (long long)y1 + D - S);
                        auto it_y3_b = lower_bound(s3.begin(), s3.end(), req_y3);
                        if (it_y3_b != s3.end()) {
                            int y3 = *it_y3_b;
                            long long L = D - S + y3;
                            long long R = 2 * S - D - y1;
                            if (L <= R) {
                                long long cut1 = x0 - (D - S);
                                long long cut2 = x0 + (D - S);
                                if (L <= cut1) {
                                    auto it = lower_bound(s2.begin(), s2.end(), L);
                                    if (it != s2.end() && *it <= min(R, cut1)) return true;
                                }
                                if (R >= cut2) {
                                    auto it = lower_bound(s2.begin(), s2.end(), max(L, cut2));
                                    if (it != s2.end() && *it <= R) return true;
                                }
                            }
                        }
                    }
                }
                return false;
            }
        };

        long long low = 1, high = 2 * S;
        int ans = 1;
        while (low <= high) {
            long long mid = low + (high - low) / 2;
            if (check(mid)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return ans;
    }
};
# @lc code=end