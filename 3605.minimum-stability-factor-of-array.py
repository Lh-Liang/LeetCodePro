#
# @lc app=leetcode id=3605 lang=python3
#
# [3605] Minimum Stability Factor of Array
#

# @lc code=start
import collections

class Solution:
    def minStable(self, nums: List[int], maxC: int) -> int:
        n = len(nums)
        if maxC >= n:
            return 0

        # Precompute primes up to sqrt(10^9)
        limit = 31622
        primes = []
        is_prime = [True] * (limit + 1)
        for p in range(2, limit + 1):
            if is_prime[p]:
                primes.append(p)
                for i in range(p * p, limit + 1, p):
                    is_prime[i] = False

        # Factorize unique values to save time
        unique_nums = set(nums)
        val_to_factors = {}
        for val in unique_nums:
            factors = []
            temp = val
            for p in primes:
                if p * p > temp:
                    break
                if temp % p == 0:
                    factors.append(p)
                    while temp % p == 0:
                        temp //= p
            if temp > 1:
                factors.append(temp)
            val_to_factors[val] = factors

        # Group indices by prime factors
        prime_to_indices = collections.defaultdict(list)
        for i, val in enumerate(nums):
            for p in val_to_factors[val]:
                prime_to_indices[p].append(i)

        # Identify maximal segments for each prime
        raw_segments = []
        for p in prime_to_indices:
            indices = prime_to_indices[p]
            if not indices: continue
            start = indices[0]
            for j in range(1, len(indices)):
                if indices[j] != indices[j-1] + 1:
                    raw_segments.append((start, indices[j-1]))
                    start = indices[j]
            raw_segments.append((start, indices[-1]))
        
        # Deduplicate and sort segments for efficiency
        all_segments = sorted(list(set(raw_segments)))

        def check(L):
            # If L=0, we must change every element >= 2
            if L == 0:
                return sum(1 for x in nums if x >= 2) <= maxC
            
            # intervals_to_hit: intervals [s, e-L] representing starting indices of stable subarrays
            intervals = []
            for s, e in all_segments:
                if e - s + 1 > L:
                    intervals.append((s, e - L))
            
            if not intervals: return True
            
            # Merge overlapping intervals [s, e-L]
            merged = []
            curr_s, curr_e = intervals[0]
            for i in range(1, len(intervals)):
                nxt_s, nxt_e = intervals[i]
                if nxt_s <= curr_e:
                    curr_e = max(curr_e, nxt_e)
                else:
                    merged.append((curr_s, curr_e))
                    curr_s, curr_e = nxt_s, nxt_e
            merged.append((curr_s, curr_e))
            
            count = 0
            last_hit = -1
            for ms, me in merged:
                # We need to pick points to cover all indices in [ms, me]
                # A point at index p covers starting indices in [p-L, p]
                # Greedily, if ms is not covered, pick point at ms + L
                start_uncovered = max(ms, last_hit + 1)
                if start_uncovered <= me:
                    # Number of points needed to cover interval [start_uncovered, me]
                    # Each point p covers a window of L+1 starting positions
                    num_needed = (me - start_uncovered) // (L + 1) + 1
                    count += num_needed
                    if count > maxC: return False
                    last_hit = start_uncovered + (num_needed - 1) * (L + 1) + L
            
            return count <= maxC

        # Binary search for the minimum stability factor L
        low, high = 0, n
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
# @lc code=end