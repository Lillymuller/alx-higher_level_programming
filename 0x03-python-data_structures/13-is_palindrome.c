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
