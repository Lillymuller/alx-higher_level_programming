#include "lists.h"

/**
 * is_palindrome - checks if singly linked list is palindrome
 * @head: pointer of singly linked list
 * Return: 0 if not, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *new = *head;
	unsigned int node = 0, i = 0;
	int data[1024];

	/* if a list doesn't exist list it is not a palindrome*/
	if (head == NULL)
		return (0);

	if (*head == NULL) /* empty list is palindrome */
		return (1);
	while (new)
	{
		new = new->next;
		node += 1;
	}
	 /* single node list is palindrome */
	if (node == 1)
		return (1);

	new = *head;
	while (new)
	{
		data[i++] = new->n;
		new = new->next;
	}
/*checking elements with their mirrored elements*/
	for (i = 0; i <= (node / 2); i++)
	{
		/*checks the value of i is same as (node - i -1)*/
		if (data[i] != data[node - i - 1])
			return (0);
	}
	return (1);
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
