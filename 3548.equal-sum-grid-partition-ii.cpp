#include <vector>
#include <numeric>
#include <algorithm>
#include <unordered_map>

using namespace std;

class Solution {
public:
    bool canPartitionGrid(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        long long total_sum = 0;
        vector<long long> row_sums(m, 0);
        vector<long long> col_sums(n, 0);
        unordered_map<int, vector<pair<int, int>>> pos_map;

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int val = grid[i][j];
                total_sum += val;
                row_sums[i] += val;
                col_sums[j] += val;
                pos_map[val].push_back({i, j});
            }
        }

        auto has_valid_cell = [&](int target_val, int r1, int r2, int c1, int c2) {
            if (target_val <= 0 || pos_map.find(target_val) == pos_map.end()) return false;
            const auto& positions = pos_map[target_val];
            
            int R = r2 - r1 + 1;
            int C = c2 - c1 + 1;

            if (R > 1 && C > 1) {
                auto it = lower_bound(positions.begin(), positions.end(), make_pair(r1, c1));
                while (it != positions.end() && it->first <= r2) {
                    if (it->second >= c1 && it->second <= c2) return true;
                    ++it;
                }
            } else if (R == 1 && C > 1) {
                for (auto& p : positions) {
                    if (p.first == r1 && (p.second == c1 || p.second == c2)) return true;
                }
            } else if (R > 1 && C == 1) {
                for (auto& p : positions) {
                    if (p.second == c1 && (p.first == r1 || p.first == r2)) return true;
                }
            } else if (R == 1 && C == 1) {
                for (auto& p : positions) {
                    if (p.first == r1 && p.second == c1) return true;
                }
            }
            return false;
        };

        auto check = [&](long long sa, int r1a, int r2a, int c1a, int c2a, int r1b, int r2b, int c1b, int c2b) {
            long long sb = total_sum - sa;
            if (sa == sb) return true;
            if (has_valid_cell((int)(sa - sb), r1a, r2a, c1a, c2a)) return true;
            if (has_valid_cell((int)(sb - sa), r1b, r2b, c1b, c2b)) return true;
            return false;
        };

        long long current_sa = 0;
        for (int i = 0; i < m - 1; ++i) {
            current_sa += row_sums[i];
            if (check(current_sa, 0, i, 0, n - 1, i + 1, m - 1, 0, n - 1)) return true;
        }

        current_sa = 0;
        for (int j = 0; j < n - 1; ++j) {
            current_sa += col_sums[j];
            if (check(current_sa, 0, m - 1, 0, j, 0, m - 1, j + 1, n - 1)) return true;
        }

        return false;
    }
};