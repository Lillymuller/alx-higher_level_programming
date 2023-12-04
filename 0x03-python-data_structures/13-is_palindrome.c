#include "lists.h"

/**
 * is_palindrome - checks if singly linked list is palindrome
 * @head: pointer of singly linked list
 * Return: 0 if not, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *new = *head;
	int cnt = 0;

	/* if a list doesn't exist list it is not a palindrome*/
	if (head == NULL)
		return (0);

	if (*head == NULL) /* empty list is palindrome */
		return (1);
	while (new->next != NULL && new->next->next != NULL)
	{
		new = new->next->next;
		cnt += 2;
	}
	 /* single node list is palindrome */
	if (new->next != NULL)
		cnt += 1;
	new = *head;
	return (palindrome_check(new, cnt));
}

/**
 * palindrome_check - recursive function to check if listint list is palidrome
 * @node_head: pointer to the current head of the list
 * @cnt: integer count of how many nodes from head to the end to check
 * Return: 1 if palindrome, 0 if not
 */

int palindrome_check(listint_t *node_head, int cnt)
{
	listint_t *node_end = node_head;
	int cnt2 = 0;

	/* move node_end  checks list fast two times at a time*/
	for (cnt2 = 0; cnt2 < cnt; cnt2++)
		node_end = node_end->next;
	/* count has successfully reached the middle, checks one step at a time */
	if (cnt <= 0)
		return (1);
	/* if mismatch is found, no palindrome */
	if (node_head->n != node_end->n)
		return (0);
	/*else, not at end of list and keep matching,go forward and call again */
	node_head = node_head->next;
	cnt -= 2;
	return (palindrome_check(node_head, cnt));
}
