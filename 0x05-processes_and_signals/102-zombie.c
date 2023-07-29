#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int infinite_while(void);

/**
 * main - Crates 5 zombie processes
 *
 * Return: Always 0 (Success)
 */

int main(void)
{
	int i = 0;

	while (i < 5)
	{
		if (fork() == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
		i++;
	}

	infinite_while();

	return (0);
}

/**
 * infinite_while - an infinite while loop
 *
 * Return: Always 0 (Success)
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
