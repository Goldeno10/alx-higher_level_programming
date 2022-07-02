#include <stdio.h>
#include <stdlib.h>
#include "lists.h"


int _len(listint_t **h)
{
	int n = 0;
	listint_t *current;

	current = *h;
	while (current != NULL)
	{
		current = current->next;
		n++;
	}
	return (n);
}

int *create_array(const listint_t *h)
{
	int i = 0;
	int *arr = NULL;

	while (h != NULL)
	{
		arr[i] = h->n;
		h = h->next;
		i++;
	}
	return (arr);
}


/**
*
*
*
*
*/

int is_palindrome(listint_t **head)
{
	int n, i, j;
	listint_t *current;
	int *arr;
	current = *head;

	if (current == NULL)
		return (0);

	n = _len(head);

	arr = create_array(current);

	for (i = 0, j = n; i <= j; i++, j--)
	{
		if (arr[i] != arr[j])
			return (1);
	}
	printf("%i", n);
	return (0);

}

