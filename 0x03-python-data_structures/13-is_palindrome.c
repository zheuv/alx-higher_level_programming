#include "lists.h"
#include <stdlib.h>

/**
 * len - Calculates the length of a linked list.
 * @head: A pointer to the head of the list.
 * Return: The length of the list.
 */
int len(listint_t **head)
{
	listint_t *current = *head;
	int i = 0;

	while (current != NULL)
	{
		i = i + 1;
		current = current->next;
	}
	return i;
}

/**
 * navigate - Navigates to a specific node in the linked list.
 * @head: The head of the list.
 * @len: The position to navigate to.
 * Return: The pointer to the desired node.
 */
listint_t *navigate(listint_t *head, int len)
{
	listint_t *current = head;

	for (int i = 1; i <= len && current != NULL; i++)
		current = current->next;

	return current;
}

/**
 * is_palindrome - Checks if a linked list is a palindrome.
 * @head: A pointer to the head of the list.
 * Return: 1 if it's a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;

	if (current == NULL)
		return 1;

	int i = 1;
	int length = len(&current);
	int loopedlen = length / 2;
	listint_t *mirror;

	while (loopedlen != 0)
	{
		mirror = navigate(current, (length - i));
		if (mirror->n != current->n)
			return 0;
		current = current->next;
		loopedlen = loopedlen - 1;
		i = i + 2;
	}
	return 1;
}

