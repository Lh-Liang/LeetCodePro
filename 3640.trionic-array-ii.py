# @lc code=start
class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return 0 # As no valid trionic subarray can exist
        
        inc = [-float('inf')]*n
        dec = [-float('inf')]*n
        post_inc = [-float('inf')]*n
        
        # Calculate inc[] array
        inc[0] = nums[0]
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                inc[i] = inc[i-1] + nums[i]
            else:
                inc[i] = nums[i]
                
        # Calculate dec[] array in reverse order
        dec[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            if nums[i] > nums[i+1]:
                dec[i] = dec[i+1] + nums[i]
            else:
                dec[i] = nums[i]
                
        # Calculate post_inc[] array in reverse order
        post_inc[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            if nums[i+1] > nums[i]:
                post_inc[i]=post_inc[i+1]+nums
            else:
                post_inc [i]=nums
       
       max_sum=float('-inf')# Find maximum sum of trionic subarray
       for q in range(2,n-1):# q is middle point)
           p_max_sum=max(inc[:q])# Max from start before q (for increasing)
           r_max_sum=max(post_inc[q:])# Max after q (for increasing)
           current_sum=p_max_sum+dec[q]+r_max_sum# Combine parts ensuring valid indices
           max_sum=max(max_sum,current_sum)# Update max_sum if current is larger
       return max_sumn