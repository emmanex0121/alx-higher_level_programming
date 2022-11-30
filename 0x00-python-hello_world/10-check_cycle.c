#include "lists.h"

/**
 * check_cycle - checks for loop in singly linked list
 * @list: singly-linked list
 *
 * Return: 0 if no loop is found and 1 if it contains a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;
	slow = fast = list;

	if (list == NULL || list->next == NULL)
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
