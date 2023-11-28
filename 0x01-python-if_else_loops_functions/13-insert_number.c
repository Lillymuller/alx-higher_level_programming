#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * insert_node - Insert node into sorted singly linked list
 * @head: pointer to head of linked list
 * @number: data for new node
 * Return: address of new node, or NULL if failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *old = NULL;
	listint_t *new = NULL;

	if (head == NULL)
		return (NULL);

/*allocating memory for new node */
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	/* if there is no linked list, creat node */
	if (*head == NULL)
	{
		*head = new;
		(*head)->next = NULL;
		return (new);
	}
/* if ther are more than one linked list, compare and add */
	old = *head;
	while (old->next != NULL)
	{
		/* if new node is smaller than first node, add */
		if (new->n < old->n)
		{
			new->next = old;
			*head = new;
			return (new);
		}

	/* if there is  one node in linked list,  compare and add*/
	if ((*head)->next == NULL)
	{
		if ((*head)->n < new->n)
			(*head)->next = new;
		else
		{
			new->next = *head;
			*head = new;
		}
		return (new);
	}
/* if new node is the same as existing node, 
   add node if not copmare and add between */
		if (((new->n > old->n) && (new->n < (old->next)->n)) ||
		    (new->n == old->n))
		{
			new->next = old->next;
			old->next = new;
			return (new);
		}
		old = old->next;
	}
/* if new node is greatest and never inserted, insert now */
	old->next = new;
	return (new);
}
