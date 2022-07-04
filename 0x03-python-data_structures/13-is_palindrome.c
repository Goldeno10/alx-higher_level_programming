#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
*dup_list - Duplicates a lnked list
*@h: The linked list head pointer
*Return: A copy of the linked list
*/
listint_t *dup_list(listint_t *h)
{

	listint_t *dup = malloc(sizeof(listint_t *));

	if (h == NULL || dup == NULL)
		return (NULL);
	dup->n = h->n;
	dup->next = dup_list(h->next);
	return (dup);
}

/**
*rev_list - Reverses a singly linked list.
*@h: List head pointer
*Return: reverse linked list
*/

listint_t *rev_list(listint_t **head)
{
	listint_t *current,*test, *prev, *next;

	current = *head;
	test = *head;
	prev = NULL;
	next = NULL;

	while (current != NULL && test != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
	return (*head);
}


/**
*is_palindrome - checks if a singly linked list is a palindrome.
*@head: The linked list head pointer
*Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/

int is_palindrome(listint_t **head)
{
	listint_t *h_node = *head;
	listint_t *rev_lst, *dup;

	if (h_node == NULL || h_node->next == NULL)
		return (1);

	dup = dup_list(*head);
	rev_lst = rev_list(&h_node);

	if (!rev_lst)
                return(1);
	while (dup != NULL && rev_lst != NULL)
	{
		if (dup->n == rev_lst->n)
		{
			dup = dup->next;
			rev_lst = rev_lst->next;
		}
		else {
			return (0);
		}
	}
	return (1);

}

