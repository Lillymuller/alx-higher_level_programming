#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if there is a cycle in singly linked list
 * Return: 0 if no cycle, 1 is yes
 */
int check_cycle(listint_t *list)
{
	listint_t *Adu = list;
	listint_t *Edu = list;

	if (list == NULL)
		return (0);

	while (1)
	{
		/*traverse(move) through nodes as long as linked list node exists*/
		if (Adu->next != NULL && Adu->next->next != NULL)
		{
			Adu = Adu->next->next;
			Edu = Edu->next;

			if (Adu == Edu) /*if nodes match, cycle found*/
				return (1);
		}
		else
			return (0);
	}

}
