#include "lists.h"

/**
 *array_reverse - reverses the content of an array of integers
 * @a: int array to reverse
 * @n: number of elements in the array
 * Return: concatenated string
 */

void array_reverse(int *ab, int n)
{
int *start = ab;
int *end;
int nods = 0;

end = ab + n - 1;
for (; start < end; start++, end--)
{
nods = *end;
*end = *start;
*start = nods;
}
}

/**
 * is_palindrome - Return 1  if palindrome, 0 if not
 * @head: linked list
 * Return: Return 1  if palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
int size, *new, *rev;
listint_t *temp = *head;

if (!head || !temp)
return (0);
if (!temp->next)
return (1);

new = malloc(sizeof(int *));
if (!new)
return (0);
rev = malloc(sizeof(int *));
if (!rev)
return (0);
for (size = 0; temp; temp = temp->next, size++)
new[size] = temp->n;

new = rev;
array_reverse(rev, size);
if (new == rev)
return (1);
return (0);
}
