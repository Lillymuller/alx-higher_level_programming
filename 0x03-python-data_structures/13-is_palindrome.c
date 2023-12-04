#include "lists.h"

/**
*reverse_listint - it reverse a siglr linked list
*@head: pointer to the first node
*Return: first node
*/

void reverse_listint(listint_t **head)
{
listint_t *end = NULL;
listint_t *begin = *head;
listint_t *next = NULL;

while (begin)
{
next = begin->next;
begin->next = end;
end = begin;
begin = next;
}
*head = end;
}

/**
* is_palindrome - checks if the single linked list is a palindrome
*@head: pinter to the first node
*Return: 1 for Success, 0 otherwise
*/

int is_palindrome(listint_t **head)
{
listint_t *node = *head, *rev = *head, *test = *head, *cpy = NULL;

if (*head == NULL || (*head)->next == NULL)
	return (1);
while (1)
{
rev = rev->next->next;
if (!rev)
{
cpy = node->next;
break;
}
if (!rev->next)
{
cpy = node->next->next;
break;
}
node = node->next;
}
reverse_listint(&cpy);

while (cpy && test)
{
if (test->n == cpy->n)
{
cpy = cpy->next;
test = test->next;
}
else
{
return (0);
}
}
if (!cpy)
return (1);

return (0);
}
