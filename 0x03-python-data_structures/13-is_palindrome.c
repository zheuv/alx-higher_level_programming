#include "lists.h"
#include <stdlib.h>

int len(listint_t **head) {
    listint_t *current = *head;
    int i = 0;

    while (current != NULL) {
        i = i + 1;
        current = current->next;
    }
    return i;
}

listint_t *naviguate(listint_t *head, int len) {
    listint_t *current = head;

    for (int i = 1; i <= len && current != NULL; i++)
        current = current->next;

    return current;
}

int is_palindrome(listint_t **head) {
    listint_t *current = *head;

    if (current == NULL)
        return 1;

    int i = 1;
    int length = len(&current);
    int loopedlen = length / 2;
    listint_t *mirror;

    while (loopedlen != 0) {
        mirror = naviguate(current, (length - i));
        if (mirror->n != current->n)
            return 0;
        current = current->next;
        loopedlen = loopedlen - 1;
        i = i + 2;
    }
    return 1;
}

