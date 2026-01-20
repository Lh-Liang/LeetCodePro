#
# @lc app=leetcode id=3762 lang=python3
#
# [3762] Minimum Operations to Equalize Subarrays
#

# @lc code=start
from bisect import bisect_right

class Solution:
    def minOperations(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        quots = [x // k for x in nums]
        rems = [x % k for x in nums]
        
        # Precompute validity check
        # A subarray is valid if all elements have the same remainder modulo k.
        # We can use a prefix sum array to check this in O(1).
        # mismatch[i] = 1 if nums[i] % k != nums[i-1] % k else 0
        mismatch = [0] * n
        for i in range(1, n):
            if rems[i] != rems[i-1]:
                mismatch[i] = 1
        
        mismatch_pref = [0] * (n + 1)
        for i in range(n):
            mismatch_pref[i+1] = mismatch_pref[i] + mismatch[i]
            
        # Merge Sort Tree Construction
        # tree[v] stores a sorted list of quotients for the range covered by node v
        # pref[v] stores the prefix sums of that sorted list
        self.tree = [[] for _ in range(4 * n)]
        self.pref = [[] for _ in range(4 * n)]
        
        def build(node, start, end):
            if start == end:
                self.tree[node] = [quots[start]]
                self.pref[node] = [0, quots[start]]
                return
            
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            
            # Merge two sorted arrays
            left_arr = self.tree[2 * node]
            right_arr = self.tree[2 * node + 1]
            merged = []
            i = j = 0
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    merged.append(left_arr[i])
                    i += 1
                else:
                    merged.append(right_arr[j])
                    j += 1
            merged.extend(left_arr[i:])
            merged.extend(right_arr[j:])
            
            self.tree[node] = merged
            
            # Build prefix sums for the merged array
            p = [0] * (len(merged) + 1)
            curr = 0
            for idx, val in enumerate(merged):
                curr += val
                p[idx+1] = curr
            self.pref[node] = p

        build(1, 0, n - 1)
        
        # Helper to get count of numbers <= val in range [L, R]
        def query_count(node, start, end, L, R, val):
            if R < start or end < L:
                return 0
            if L <= start and end <= R:
                return bisect_right(self.tree[node], val)
            mid = (start + end) // 2
            return query_count(2 * node, start, mid, L, R, val) + \
                   query_count(2 * node + 1, mid + 1, end, L, R, val)

        # Helper to find the k-th smallest number (0-indexed rank) in range [L, R]
        # We binary search on the answer space (min_val to max_val)
        min_val = min(quots)
        max_val = max(quots)
        
        def get_quantile(L, R, rank):
            low = min_val
            high = max_val
            ans = high
            
            while low <= high:
                mid = (low + high) // 2
                # count how many numbers are <= mid inside [L, R]
                c = query_count(1, 0, n - 1, L, R, mid)
                if c > rank:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return ans

        # Helper to get sum and count of numbers <= val in range [L, R]
        def query_sum_count(node, start, end, L, R, val):
            if R < start or end < L:
                return 0, 0
            if L <= start and end <= R:
                idx = bisect_right(self.tree[node], val)
                return self.pref[node][idx], idx
            
            mid = (start + end) // 2
            s1, c1 = query_sum_count(2 * node, start, mid, L, R, val)
            s2, c2 = query_sum_count(2 * node + 1, mid + 1, end, L, R, val)
            return s1 + s2, c1 + c2

        ans = []
        for l, r in queries:
            # Check validity
            # If mismatch_pref[r+1] - mismatch_pref[l+1] > 0, it means there's a mismatch inside
            # Actually, mismatch at index i compares i and i-1.
            # For range [l, r], we need to check mismatches at l+1, l+2, ..., r.
            # So we look at mismatch_pref[r+1] - mismatch_pref[l+1].
            # If l == r, valid automatically.
            if l < r and (mismatch_pref[r+1] - mismatch_pref[l+1] > 0):
                ans.append(-1)
                continue
            
            # Find Median
            count = r - l + 1
            median_rank = count // 2  # 0-indexed rank of median
            median_val = get_quantile(l, r, median_rank)
            
            # Calculate Cost
            # Cost = sum(|x - median|) for x in range
            #      = (count_less * median - sum_less) + (sum_greater - count_greater * median)
            # where less includes equal to median for simplicity in splitting, 
            # but strictly speaking |x - median| is 0 for x=median so it doesn't matter which side equal goes.
            
            sum_less, count_less = query_sum_count(1, 0, n - 1, l, r, median_val)
            
            # Total sum of the range [l, r]
            # We can get total sum by querying with infinity or just reuse the logic
            # Actually, sum_greater = total_sum - sum_less
            # count_greater = total_count - count_less
            
            # To get total sum efficiently, we can use a standard prefix sum array for quots
            # let's build it on the fly or precompute it. Precomputing is better.
            
            # But wait, query_sum_count gives us sum of subset.
            # We need total sum of quots[l...r].
            # Let's add a simple prefix sum array for quots.
            pass 

        # Add simple prefix sum for quots
        quot_pref = [0] * (n + 1)
        for i in range(n):
            quot_pref[i+1] = quot_pref[i] + quots[i]

        ans = []
        for l, r in queries:
            if l < r and (mismatch_pref[r+1] - mismatch_pref[l+1] > 0):
                ans.append(-1)
                continue
            
            count = r - l + 1
            median_rank = count // 2 
            median_val = get_quantile(l, r, median_rank)
            
            sum_le, cnt_le = query_sum_count(1, 0, n - 1, l, r, median_val)
            
            total_sum = quot_pref[r+1] - quot_pref[l]
            sum_gt = total_sum - sum_le
            cnt_gt = count - cnt_le
            
            cost = (cnt_le * median_val - sum_le) + (sum_gt - cnt_gt * median_val)
            ans.append(cost)
            
        return ans
# @lc code=end