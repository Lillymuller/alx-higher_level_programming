#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Insert node into sorted singly linked list
 * @head: pointer to head of linked list
 * @number: data for new node
 * Return: address of new node, or NULL if failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *old = *head;
	unsigned int i = 0;

	if (!(old) || (*old).n > number)
	{
		new = malloc(sizeof(listint_t));
		if (new == NULL)
			return (NULL);

		(*new).n = number;
		(*new).next = *head;

		*head = new;

		return (*head);
	}

	while (old)
	{
		if (!((*old).next) || (*old).next->n > number)
		{
			new = malloc(sizeof(listint_t));
			if (new == NULL)
				return (NULL);
			(*new).n = number;
			(*new).next = (*old).next;
			(*old).next = new;
			return (new);
		}
		old = (*old).next;
		i++;
	}

	return (NULL);
}
