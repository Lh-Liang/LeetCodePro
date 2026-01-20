#
# @lc app=leetcode id=2074 lang=cpp
#
# [2074] Reverse Nodes in Even Length Groups
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
    ListNode* reverseEvenLengthGroups(ListNode* head) {
        // The first group (length 1) is never reversed because 1 is odd.
        // We start with prev pointing to the first node (head).
        ListNode* prev = head;
        int g = 2; // The next group target length is 2

        while (prev->next) {
            // 1. Identify how many nodes are actually in the current group
            int actualCount = 0;
            ListNode* temp = prev->next;
            while (temp && actualCount < g) {
                temp = temp->next;
                actualCount++;
            }

            if (actualCount % 2 == 0) {
                // 2. Reverse the group if its actual length is even
                ListNode* curr = prev->next; // This will become the tail after reversal
                ListNode* node = curr;
                ListNode* rev_prev = nullptr;
                for (int i = 0; i < actualCount; ++i) {
                    ListNode* next_node = node->next;
                    node->next = rev_prev;
                    rev_prev = node;
                    node = next_node;
                }
                // Link the node before the group to the new head (rev_prev)
                // and link the new tail (curr) to the start of the next group (node)
                prev->next = rev_prev;
                curr->next = node;
                // Move prev to the tail of the processed group
                prev = curr;
            } else {
                // 3. If the length is odd, skip the nodes
                for (int i = 0; i < actualCount; ++i) {
                    prev = prev->next;
                }
            }
            
            // 4. Increment target group length for the next iteration
            g++;
        }

        return head;
    }
};
# @lc code=end