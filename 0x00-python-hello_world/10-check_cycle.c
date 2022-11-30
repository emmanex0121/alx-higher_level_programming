#include "lists.h"

/**
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
