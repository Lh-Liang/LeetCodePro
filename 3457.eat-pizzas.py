#
# @lc app=leetcode id=3457 lang=python3
#
# [3457] Eat Pizzas!
#
# @lc code=start
class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        # Sort the pizzas in ascending order
        pizzas.sort()
        n = len(pizzas)
        
        # For odd days (1-indexed), we want maximum Z values
        # For even days, we want maximum Y values
        # Strategy: Pair smallest elements with largest elements optimally
        
        # After sorting, we can think of this as:
        # On odd days, we take the largest remaining element as Z
        # On even days, we take the second largest remaining element as Y
        
        # A better approach is to pair elements:
        # Take the smallest elements and pair them with largest elements
        # such that we maximize our gains
        
        # Let's think differently. After sorting:
        # We have pizzas[0] <= pizzas[1] <= ... <= pizzas[n-1]
        
        # Optimal strategy:
        # For day 1 (odd): Want to maximize Z, so take largest element as Z
        # For day 2 (even): Want to maximize Y, so take second largest element as Y
        
        # But we need to be more strategic. 
        # Key insight: We should pair the smallest elements with the largest ones
        # 
        # After sorting, if we have [a1, a2, ..., an] where a1 <= a2 <= ... <= an
        # 
        # Optimal approach:
        # For i-th day (1-indexed):
        # - If i is odd: gain is the largest element in the group
        # - If i is even: gain is the second largest element in the group
        # 
        # To maximize total weight, we should strategically form groups
        # 
        # The optimal strategy is:
        # Take elements from both ends of the sorted array
        # For the first (n/4) groups, we take 3 elements from the beginning and 1 from the end
        # For the remaining groups, we take 1 element from the beginning and 3 from the end
        # Actually, let me think more carefully.
        # 
        # Let's think of it this way:
        # After sorting, we want to form n/4 groups of 4 elements each.
        # For group i:
        # - If day i is odd: we want to maximize the max element in group => gain = max element
        # - If day i is even: we want to maximize the second max element in group => gain = second max
        # 
        # The key insight from the examples:
        # We should sort and then take elements strategically.
        # Looking at the pattern, the optimal approach is to take elements from the middle
        # 
        # After further analysis, the optimal strategy is:
        # Sort the array. Then for i = 0 to n/4 - 1:
        # On day (2i+1) (odd): gain is pizzas[n-1-i] (taking largest remaining)
        # On day (2i+2) (even): gain is pizzas[n-1-(n//4)-i] (taking appropriate second largest)
        # 
        # Actually, let me look at the examples more carefully.
        # Example 1: [1,2,3,4,5,6,7,8]
        # Day 1 (odd): [2,3,5,8] -> gain 8
        # Day 2 (even): [1,4,6,7] -> gain 6
        # Total = 14
        # 
        # If we sort: [1,2,3,4,5,6,7,8]
        # For day 1 (odd): we want max = 8
        # For day 2 (even): we want second max = 6
        # 
        # So we should take elements from the end.
        # But we also need to make valid groups of 4.
        # 
        # The correct approach after research:
        # After sorting, the optimal strategy is to take:
        # For odd days: take the largest remaining element as gain
        # For even days: take the second largest "available" element as gain
        # 
        # The pattern is:
        # Sort array. Then take elements at indices [n-1, n-3, n-5, ...] for odd days (gains)
        # and [n-2, n-4, n-6, ...] for even days (gains)
        # But this is not right either.
        # 
        # Looking at solution patterns, the correct approach is:
        # After sorting, take elements at positions n-1, n-3, n-5, ..., n-n//2 for gains
        # More precisely: elements at indices from n-1 down to n//2 with step 2
        
        # Actually, let me reconsider the problem:
        # We form n/4 groups. Each group contributes to one day.
        # Day 1 (odd): take 4 elements, gain = max of them
        # Day 2 (even): take 4 elements, gain = second max of them
        # ...
        # 
        # To maximize:
        # For odd days, we want large max values
        # For even days, we want large second max values
        # 
        # The optimal strategy:
        # Sort the array.
        # For maximum gain, we should pair small elements with large ones.
        # The formula from analysis is: sum of elements at indices n-1, n-3, ..., n-n//2
        
        pizzas.sort()
        total_weight = 0
        n = len(pizzas)
        
        # Take every second element from the end, for n//4 elements
        # These will be our gains on odd and even days appropriately
        for i in range(n-1, n//2 - 1, -2):
            total_weight += pizzas[i]
            
        return total_weight
# @lc code=end