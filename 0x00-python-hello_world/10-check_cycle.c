#include "lists.h"
/**
 * check_cycle - a fun to check if a linked list has a cycle
 * @list: list to be checked
 * Return: 0(no cycle) or 1(has cycle)
 */
int check_cycle(listint_t *list)
{
	listint_t *chk1 = list;
	listint_t *chk2 = list;

	if (!list)
	{
		return (0);
	}

	while (chk1 && chk2 && chk1->next)
	{
		chk2 = chk2->next;
		chk1 = chk1->next;
		chk1 = chk1->next;
		if(chk1 == chk2)
		{
			return (1);
		}
		return (0);
	}
