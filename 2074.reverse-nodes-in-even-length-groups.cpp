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
        ListNode dummy(0, head);
        ListNode* prev = &dummy;
        ListNode* curr = head;
        int groupSize = 1;
        while (curr) {
            // Identify group boundaries
            ListNode* groupStart = curr;
            int cnt = 0;
            ListNode* temp = curr;
            for (int i = 0; i < groupSize && temp; ++i) {
                temp = temp->next;
                ++cnt;
            }
            ListNode* groupEndNext = temp;
            // Reverse if even
            if (cnt % 2 == 0) {
                ListNode* prevRev = groupEndNext;
                ListNode* node = curr;
                for (int i = 0; i < cnt; ++i) {
                    ListNode* nextNode = node->next;
                    node->next = prevRev;
                    prevRev = node;
                    node = nextNode;
                }
                prev->next = prevRev;
                prev = groupStart;
                curr = groupEndNext;
            } else {
                for (int i = 0; i < cnt; ++i) {
                    prev = curr;
                    curr = curr->next;
                }
            }
            // Verify pointer correctness after each group
            // (Implicit in code: prev is at group tail, curr is at next group head)
            ++groupSize;
        }
        // Final validation: dummy.next is the new head
        return dummy.next;
    }
};
# @lc code=end