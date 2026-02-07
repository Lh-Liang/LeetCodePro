#
# @lc app=leetcode id=2807 lang=cpp
#
# [2807] Insert Greatest Common Divisors in Linked List
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
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        if (!head || !head->next) return head; // If there's only one node, return as-is.
        ListNode *current = head;
        while (current && current->next) {
            int gcdValue = gcd(current->val, current->next->val); // Calculate GCD of two adjacent nodes.
            ListNode *newNode = new ListNode(gcdValue); // Create a new node with this GCD value.
            newNode->next = current->next; // Insert this node between current and current->next.
            current->next = newNode; // Move to next pair.
            current = newNode->next; // Move to next original node in the sequence.
        }
        return head; // Return the modified list starting from head.
    }
private:
    int gcd(int a, int b) { // Helper function to compute greatest common divisor using Euclidean algorithm. // while (b != 0) { // int temp = a % b; // a = b; // b = temp; // } // return a; // } // }; // @lc code=end