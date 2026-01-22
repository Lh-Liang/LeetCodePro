#
# @lc app=leetcode id=3420 lang=cpp
#
# [3420] Count Non-Decreasing Subarrays After K Operations
#

#include <vector>
#include <deque>
using namespace std;

// @lc code=start
class Solution {
public:
    long long countNonDecreasingSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        vector<long long> pref(n + 1);
        pref[0] = 0;
        for(int i = 0; i < n; ++i)
            pref[i + 1] = pref[i] + nums[i];
        
        auto getSum = [&](int l,int r)->long long{
            return pref[r + 1] - pref[l];
        };
        
        deque<int> dq;
        long long ans = 0;
        int curr_left = 0;
        long long total_record_sum = 0;
        
        auto calc_total_from_dq = [&](int curr_right)->long long{
            long long res = 0;
            int sz = dq.size();
            for(int ii = 0; ii < sz; ++ii){
                int idx = dq[ii];
                int nxt_idx = (ii == sz - 1)? curr_right + 1 : dq[ii + 1];
                res += static_cast<long long>(nums[idx]) * static_cast<long long>(nxt_idx - idx);
            }
            return res;
        };
        
        auto get_deficit = [&](int curr_left,int curr_right)->long long{
            return total_record_sum - getSum(curr_left, curr_right);
        };
        
        auto add_right = [&](int idx){
            int x = nums[idx];
            // extend last segment
            if(!dq.empty()){
                int last_idx = dq.back();
                long long last_val = static_cast<long long>(nums[last_idx]);
                total_record_sum += last_val * 1LL;
            }
            
            while(!dq.empty() && static_cast<long long>(nums[dq.back()]) <= static_cast<long long>(x)){
                int popped_idx = dq.back();
                dq.pop_back();
                // recalc necessary
                // recalc after finish pops
            }
            
            // push idx
            dq.push_back(idx);
            
            // recalc entire total_record_sum
            total_record_sum = calc_total_from_dq(idx);
        };
        
        auto remove_left = [&](int idx){
            bool changed_front = false;
            if(!dq.empty() && dq.front() == idx){
                changed_front = true;
                dq.pop_front();
            }
            // Recalc entire total_record_sum
            // Note: curr_right hasn't changed
            int curr_right = idx;
            if(curr_left < n && curr_left <= curr_right){
                total_record_sum = calc_total_from_dq(curr_right);
            }
        };
        
        
        for(int curr_right = 0; curr_right < n; ++curr_right){
            add_right(curr_right);
            
            while(get_deficit(curr_left, curr_right) > static_cast<long long>(k)){
                remove_left(curr_left);
                ++curr_left;
                
                // ensure curr_left doesn't exceed curr_right
                if(curr_left > curr_right){
                    break;
                }
            }
            
            ans += static_cast<long long>(curr_right - curr_left + 1);
        }
        return ans;
    }
};
// @lc code=end