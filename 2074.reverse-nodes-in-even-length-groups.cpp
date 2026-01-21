#include <bits/stdc++.h>
using namespace std;

// @lc app=leetcode id=2074 lang=cpp
//
// [2074] Reverse Nodes in Even Length Groups
//

// @lc code=start
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
    // Reverse exactly n nodes starting at head.
    // Returns {newHead, newTail, successorAfterReversedPart}
    tuple<ListNode*, ListNode*, ListNode*> reverseN(ListNode* head, int n) {
        ListNode* prev = nullptr;
        ListNode* curr = head;
        while (n-- > 0 && curr) {
            ListNode* nxt = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nxt;
        }
        // prev is new head, head is now tail, curr is successor
        return {prev, head, curr};
    }

    ListNode* reverseEvenLengthGroups(ListNode* head) {
        ListNode dummy(0);
        dummy.next = head;

        ListNode* prev = &dummy;
        int k = 1;

        while (prev->next) {
            ListNode* start = prev->next;
            ListNode* curr = start;
            ListNode* end = nullptr;
            int len = 0;

            // Determine actual length of this group and the end pointer
            while (len < k && curr) {
                end = curr;
                curr = curr->next;
                len++;
            }
            ListNode* nextGroup = curr; // node after the group

            if (len % 2 == 0) {
                auto [newHead, newTail, succ] = reverseN(start, len);
                prev->next = newHead;
                newTail->next = succ; // succ should equal nextGroup
                prev = newTail;
            } else {
                prev = end;
            }

            k++;
        }

        return dummy.next;
    }
};
// @lc code=end
