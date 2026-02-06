#
# @lc app=leetcode id=3768 lang=python3
#
# [3768] Minimum Inversion Count in Subarrays of Fixed Length
#

# @lc code=start
class Solution:
    def minInversionCount(self, nums: List[int], k: int) -> int:
        def coordinate_compress(nums):
            unique_nums = sorted(set(nums))
            return {num: i + 1 for i, num in enumerate(unique_nums)}
        
        def add(fenwick_tree, index, value):
            while index < len(fenwick_tree):
                fenwick_tree[index] += value
                index += index & (-index)
        
        def sum(fenwick_tree, index):
            total = 0
            while index > 0:
                total += fenwick_tree[index]
                index -= index & (-index)
            return total
        
        def count_inversions(arr):
            inv_count = 0
            fenwick_tree = [0] * (len(arr) + 1)
            compressed_arr = [value_map[num] for num in arr]
            for i in reversed(range(len(compressed_arr))):
                inv_count += sum(fenwick_tree, compressed_arr[i] - 1)
                add(fenwick_tree, compressed_arr[i], 1)
            return inv_count
        
        n = len(nums)
        min_inversions = float('inf')
        value_map = coordinate_compress(nums)
        current_subarray = nums[:k]
        current_inv_count = count_inversions(current_subarray)
        min_inversions = min(min_inversions, current_inv_count)
         # Sliding window approach to update inversion count efficiently  fenwick_tree=[0]*(len(value_map)+1 )  compressed_arr=[value_map[num]for num in nums ] # Initialize the Fenwick Tree with the first k elements' inversions  for num in compressed_arr[:k]: add(fenwick_tree,num,+1 ) # Iterate over each sliding window position starting from the second window  for i in range(k,n ): # Remove the element going out of the window from Fenwick Tree influence  outgoing_value=compressed_arr[i-k ] add(fenwick_tree,outgoing_value,-1 ) current_inv_count-=sum(fenwick_tree,outgoing_value)-sum(fenwick_tree,outgoing_value-1 ) # Add new element coming into the window incoming_value=compressed_arr[i ] current_inv_count+=sum(fenwick_tree,len(value_map))-sum(fenwick_tree,incoming_value ) add(fenwick_tree,incoming_value,+1 ) min_inversions=min(min_inversions,current_inv_count ) return min_inversions # @lc code=end