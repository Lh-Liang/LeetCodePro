#
# @lc app=leetcode id=3748 lang=python3
#
# [3748] Count Stable Subarrays
#

# @lc code=start
class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        if n == 0:
            return [0] * len(queries)
        
        # Identify segments
        # A segment is a maximal contiguous subarray that is non-decreasing.
        segments = []
        start = 0
        for i in range(n - 1):
            if nums[i] > nums[i+1]:
                segments.append((start, i))
                start = i + 1
        segments.append((start, n - 1))
        
        # Map each index to its segment ID
        # Since segments are contiguous and cover 0 to n-1, we can fill an array.
        # However, filling an array of size 10^5 is fine.
        segment_ids = [0] * n
        for sid, (s, e) in enumerate(segments):
            for i in range(s, e + 1):
                segment_ids[i] = sid
        
        # Precompute prefix sums of the stable subarray counts for full segments
        # Contribution of a segment of length l is l*(l+1)//2
        segment_contributions = []
        for s, e in segments:
            length = e - s + 1
            segment_contributions.append(length * (length + 1) // 2)
        
        # Prefix sum array for segment contributions
        # prefix_sums[k] = sum of contributions of segments 0 to k-1
        prefix_sums = [0] * (len(segments) + 1)
        for i in range(len(segments)):
            prefix_sums[i+1] = prefix_sums[i] + segment_contributions[i]
            
        ans = []
        for l, r in queries:
            sid_l = segment_ids[l]
            sid_r = segment_ids[r]
            
            if sid_l == sid_r:
                # Entire query range is within one stable segment
                length = r - l + 1
                ans.append(length * (length + 1) // 2)
            else:
                res = 0
                
                # Left partial segment
                # The segment sid_l ends at segments[sid_l][1]
                # The part within [l, r] is [l, segments[sid_l][1]]
                e_l = segments[sid_l][1]
                len_l = e_l - l + 1
                res += len_l * (len_l + 1) // 2
                
                # Right partial segment
                # The segment sid_r starts at segments[sid_r][0]
                # The part within [l, r] is [segments[sid_r][0], r]
                s_r = segments[sid_r][0]
                len_r = r - s_r + 1
                res += len_r * (len_r + 1) // 2
                
                # Middle full segments
                # Segments from sid_l + 1 to sid_r - 1
                if sid_l + 1 < sid_r:
                    res += prefix_sums[sid_r] - prefix_sums[sid_l + 1]
                
                ans.append(res)
                
        return ans
# @lc code=end