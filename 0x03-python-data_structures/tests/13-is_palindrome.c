#include <stdlib.h>
#include <stdio.h>
#include "Lists.h"

/**
 * is_palindrome - Function that checks if a list is a palindrome
 * @head: Head list
 * 
 * Return: 0 if not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *new;

	new = head;
	if(head)
	{
		if (head == NULL || head->next == NULL)
			return (0);
		else
			return (1);
	}
}
