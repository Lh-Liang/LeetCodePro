#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

class Solution {
public:
    int totalSteps(vector<int>& nums) {
        int n = nums.size();
        int ans = 0;
        // The stack will store pairs of {value, steps}, where 'steps' is the 
        // number of steps it takes for the current element to be removed.
        stack<pair<int, int>> st;
        
        for (int i = 0; i < n; ++i) {
            int current_steps = 0;
            
            // While the current element is greater than or equal to the top of the stack, 
            // it pops the top element and updates the 'current_steps' to be the 
            // maximum steps of the popped elements. This represents the time needed 
            // for the elements between the next greater element and the current element to be removed.
            while (!st.empty() && st.top().first <= nums[i]) {
                current_steps = max(current_steps, st.top().second);
                st.pop();
            }
            
            if (st.empty()) {
                // If no element to the left is strictly greater than nums[i], it won't be removed.
                current_steps = 0;
            } else {
                // If there is a greater element, nums[i] will be removed in the step 
                // after all intermediate elements are gone.
                current_steps = current_steps + 1;
            }
            
            ans = max(ans, current_steps);
            st.push({nums[i], current_steps});
        }
        
        return ans;
    }
};