#include "lists.h"

/**
*check_cycle - checks if a singly linked list has a cycle in it
*@list: A linked list under test
*Return: 0 if there is no cycle, 1 if there is a cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *fast;
	listint_t *twice_fast;

	if (!list)
		return (0);

	fast = list;
	twice_fast = list;

	while (fast != NULL && twice_fast != NULL && twice_fast->next != NULL)
	{
		fast = fast->next;
		twice_fast = twice_fast->next->next;
		if (fast == twice_fast)
			return (1);
	}
	return (0);
}
