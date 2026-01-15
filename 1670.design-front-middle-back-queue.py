#
# @lc app=leetcode id=1670 lang=python3
#
# [1670] Design Front Middle Back Queue
#
# @lc code=start
class FrontMiddleBackQueue:
    def __init__(self):
        self.front = []  # left half, front at end
        self.back = []   # right half, back at end
    
    def _balance(self):
        # Ensure len(front) == len(back) or len(front) == len(back) + 1
        if len(self.front) > len(self.back) + 1:
            # move one from front to back
            self.back.insert(0, self.front.pop(0))
        elif len(self.front) < len(self.back):
            # move one from back to front
            self.front.append(self.back.pop(0))
    
    def pushFront(self, val: int) -> None:
        self.front.append(val)
        self._balance()
    
    def pushMiddle(self, val: int) -> None:
        # Insert into frontmost middle position
        if len(self.front) == len(self.back):
            self.front.append(val)
        else:
            # len(front) > len(back), need to move last of front to back? Actually we want to insert at the middle.
            # The middle index is (len(front)+len(back)) // 2. Since we have two halves, we can think of inserting into front at appropriate position.
            # When total length is odd, middle is the last element of front (since we keep front longer by at most 1).
            # So we need to insert at the end of front? Wait, example: pushMiddle into [1,2,3,4,5] (front=[1,2,3], back=[4,5]? Actually we need to represent queue as list.
            # Let's define: front holds first half such that its last element is the middle when total odd.
            # For pushMiddle: if len(front) == len(back), then new middle becomes after the current middle? Actually example: push 6 into middle of [1,2,3,4,5] -> [1,2,6,3,4,5].
            # Original queue length 5 (odd). The middle is the third element (index 2). After insertion, length 6 (even), and new middle is between index 2 and 3? But they insert at index 2? Actually they inserted before the original middle? Let's see: [1,2,3,4,5] -> insert 6 in middle -> [1,2,6,3,4,5]. The original middle was 3 (index 2). After insertion, 6 is at index 2 and 3 moves to index 3. So they inserted before the original middle.
            # With our representation: let's keep front as first half including middle when odd. So for length 5: front = [1,2,3], back = [4,5]. Middle is last of front (3). To insert before middle (so that new element becomes middle and original middle shifts right), we need to insert at the end of front? Actually we want new element to be placed before the current middle. That means we should insert at position len(front)-1? Wait.
            # Better approach: use two deques and maintain invariant that front size is either equal to back size or one more.
            # For pushMiddle: if sizes equal -> push to back of front (i.e., append to front). If sizes not equal (front larger by one) -> push to front of back (i.e., insert at beginning of back).
            # Let's test with example: initial queue empty -> pushFront(1): front=[1], back=[], sizes: front=1 back=0. pushBack(2): after balance? Actually we need to define operations.
            # Let's implement using two deques with collections.deque for efficient pops from both ends.
            pass
        
        # I realize my initial approach with lists is inefficient due to O(n) inserts/pops at beginning.
        # I'll switch to using collections.deque for both halves."
except Exception as e:"