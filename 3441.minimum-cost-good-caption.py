#
# @lc app=leetcode id=3441 lang=python3
#
# [3441] Minimum Cost Good Caption
#

# @lc code=start
class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        n = len(caption)
        if n < 3:
            return ""
        
        # Convert string to list for easier manipulation
        s = list(caption)
        
        # Try all 26 lowercase letters as the starting character
        best_result = None
        min_cost = float('inf')
        
        for start_char in range(26):
            start_letter = chr(ord('a') + start_char)
            # Try both directions: start_letter and start_letter+1 as the two characters
            for first_char_code in [start_char, min(25, start_char + 1)]:
                first_char = chr(ord('a') + first_char_code)
                second_char_code = first_char_code - 1 if first_char_code > 0 else (first_char_code + 1)
                second_char = chr(ord('a') + second_char_code)
                
                # Generate candidate string alternating between first_char and second_char
                candidate = []
                for i in range(n):
                    if i % 2 == 0:
                        candidate.append(first_char)
                    else:
                        candidate.append(second_char)
                
                # Check if this pattern can form groups of at least 3
                valid = True
                i = 0
                while i < n:
                    j = i
                    while j < n and candidate[j] == candidate[i]:
                        j += 1
                    if j - i < 3:
                        valid = False
                        break
                    i = j
                
                if not valid:
                    continue
                
                # Calculate cost
                cost = 0
                for i in range(n):
                    if s[i] != candidate[i]:
                        cost += 1
                
                # Update best result
                if cost < min_cost or (cost == min_cost and ''.join(candidate) < (best_result or '')):
                    min_cost = cost
                    best_result = ''.join(candidate)
        
        # Another approach: try making all characters the same
        for c in range(26):
            target_char = chr(ord('a') + c)
            candidate = [target_char] * n
            
            # Check if valid (all same char, so length must be >= 3)
            if n < 3:
                continue
                
            # Calculate cost
            cost = 0
            for i in range(n):
                if s[i] != candidate[i]:
                    cost += 1
            
            # Update best result
            if cost < min_cost or (cost == min_cost and ''.join(candidate) < (best_result or '')):
                min_cost = cost
                best_result = ''.join(candidate)
        
        return best_result or ""
# @lc code=end