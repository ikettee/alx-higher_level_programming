#include "lists.h"

/**
 * check_cycle - function that checks if a linked list contains a cycle
 * @list: the linked list to check
 * Return: should be 1 if the list has a cycle, otherwise 0
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
