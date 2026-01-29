#
# @lc app=leetcode id=3782 lang=python3
#
# [3782] Last Remaining Integer After Alternating Deletion Operations
#

# @lc code=start
class Solution:
    def lastInteger(self, n: int) -> int:
        # The sequence is always an Arithmetic Progression (AP).
        # head: the first element of the current AP.
        # step: the common difference between elements.
        # count: total number of elements in the current AP.
        head = 1
        step = 1
        count = n
        left_to_right = True
        
        # Time Complexity: O(log n) as count is halved each iteration.
        # Space Complexity: O(1).
        while count > 1:
            if left_to_right:
                # Operation 1: Starting from left, delete every second number (2nd, 4th...).
                # The first element (head) is always kept.
                pass
            else:
                # Operation 2: Starting from right, delete every second number (2nd, 4th... from right).
                # If count is even (e.g., 4 elements), the 2nd from right is the 3rd from left,
                # and the 4th from right is the 1st from left (head). So head is deleted.
                # If count is odd (e.g., 3 elements), the 2nd from right is the 2nd from left.
                # The 1st and 3rd from left are kept. So head is kept.
                if count % 2 == 0:
                    head += step
            
            # In both operations, exactly half (if even) or the smaller half (if odd) are removed.
            # Specifically, we always keep (count + 1) // 2 elements.
            count = (count + 1) // 2
            step *= 2
            left_to_right = not left_to_right
            
        return head
# @lc code=end