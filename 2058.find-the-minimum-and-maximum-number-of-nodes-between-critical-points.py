class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # A critical point needs at least 3 nodes to exist
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        first_cp_index = -1
        last_cp_index = -1
        min_dist = float('inf')
        
        # Initialize pointers and index tracking
        prev_val = head.val
        curr_node = head.next
        curr_index = 1
        
        # Iterate through the list until the second-to-last node
        while curr_node.next:
            next_val = curr_node.next.val
            curr_val = curr_node.val
            
            # Check if current node is a local maxima or local minima
            is_critical = (curr_val > prev_val and curr_val > next_val) or \
                          (curr_val < prev_val and curr_val < next_val)
            
            if is_critical:
                if first_cp_index == -1:
                    # Record the first critical point found
                    first_cp_index = curr_index
                else:
                    # Update minimum distance between adjacent critical points
                    min_dist = min(min_dist, curr_index - last_cp_index)
                
                # Update the index of the most recent critical point
                last_cp_index = curr_index
            
            # Move pointers forward
            prev_val = curr_val
            curr_node = curr_node.next
            curr_index += 1
            
        # If fewer than two critical points were found, return [-1, -1]
        if min_dist == float('inf'):
            return [-1, -1]
        
        # Maximum distance is the distance between the first and last critical points
        max_dist = last_cp_index - first_cp_index
        
        return [int(min_dist), max_dist]