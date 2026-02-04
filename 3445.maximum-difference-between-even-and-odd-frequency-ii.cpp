# @lc code=start
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        from collections import defaultdict
        n = len(s)
        max_diff = float('-inf')
        freq = defaultdict(int)
        
        # Step 2: Initialize frequency map for first k-length substring
        for i in range(k):
            freq[s[i]] += 1
        
        def find_max_diff(freq):
            odd_freq_chars = [char for char, count in freq.items() if count % 2 != 0]
            even_freq_chars = [char for char, count in freq.items() if count % 2 == 0 and count > 0]
            max_local_diff = float('-inf')
            for odd_char in odd_freq_chars:
                for even_char in even_freq_chars:
                    diff = freq[odd_char] - freq[even_char]
                    max_local_diff = max(max_local_diff, diff)
            return max_local_diff
        
        # Step 3 & 5: Slide window and calculate differences
        max_diff = find_max_diff(freq)
        for start in range(1, n - k + 1):
            outgoing_char = s[start - 1]
            incoming_char = s[start + k - 1]
            
            # Update frequencies
            freq[outgoing_char] -= 1
            if freq[outgoing_char] == 0:
                del freq[outgoing_char]
            freq[incoming_char] += 1
            
            # Step 4 & 5: Calculate current max difference
            current_diff = find_max_diff(freq)
            max_diff = max(max_diff, current_diff)
        
        # Step 6: Return result
        return max_diff if max_diff != float('-inf') else -1
# @lc code=end