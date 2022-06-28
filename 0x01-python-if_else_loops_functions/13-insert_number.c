#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - adds a new node to a listint_t list
 * @head: pointer to a pointer of the start of the list
 * @number: integer to be included in node
 * Return: address of the new element or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = *head;
	*head = new;

	return (new);
}
