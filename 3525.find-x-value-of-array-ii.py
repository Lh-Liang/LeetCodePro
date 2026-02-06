#
# @lc app=leetcode id=3525 lang=python3
#
# [3525] Find X Value of Array II
#
# @lc code=start
class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        result = []
        n = len(nums)
        
        for query in queries:
            indexi, valuei, starti, xi = query
            # Update nums with new value at indexi
            nums[indexi] = valuei
            
            # Calculate x-value for current configuration of nums[starti:]
            current_x_value = self.calculate_x_value(nums[starti:], k, xi)
            result.append(current_x_value)
        return result
    
    def calculate_x_value(self, nums: List[int], k: int, x: int) -> int:
        count_ways = 0
        current_product_mod_k = 1  # Product modulo k of current suffix elements
        
        # Calculate number of valid suffix removals by iterating from end to start
        for num in reversed(nums):
            if current_product_mod_k == x:
                count_ways += 1
            current_product_mod_k = (current_product_mod_k * num) % k
        if current_product_mod_k == x:  # Check full product case as well
            count_ways += 1
        return count_ways
# @lc code=end