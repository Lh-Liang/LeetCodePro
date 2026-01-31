#
# @lc app=leetcode id=2816 lang=cpp
#
# [2816] Double a Number Represented as a Linked List
#

# @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* doubleIt(ListNode* head) {
        // If the head value is >= 5, doubling it will create a new leading digit (1).
        // We can prepend a node with value 0 to handle this uniformly.
        if (head->val >= 5) {
            head = new ListNode(0, head);
        }
        
        ListNode* curr = head;
        while (curr != nullptr) {
            // Double the current value and keep only the unit digit.
            curr->val = (curr->val * 2) % 10;
            
            // If the next node's value is 5 or more, it will produce a carry.
            // Add that carry to the current node.
            if (curr->next != nullptr && curr->next->val >= 5) {
                curr->val++;
            }
            
            curr = curr->next;
        }
        
        return head;
    }
};
# @lc code=end