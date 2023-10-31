#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a node into a sorted singly linked list
 * @head: A pointer to the head of the list
 * @number: The value to insert into the list
 * Return: A pointer to the new node or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current;
	int value;
	int value2;

	current = *head;
	new_node = malloc(sizeof(listint_t));
	
	if (new_node == NULL)
		return (NULL);
	
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	while (current->next != NULL)
	{
		value = current->n;
		value2 = current->next->n;

		if (number > value && number <= value2)
		{
			new_node->next = current->next;
			current->next = new_node;
			return (new_node);
		}

		current = current->next;
	}

	current->next = new_node;
	return (new_node);
}

