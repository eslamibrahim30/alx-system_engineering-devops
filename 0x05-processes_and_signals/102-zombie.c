#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <signal.h>
#include <unistd.h>

/**
 * infinite_while - Just infinite while loop.
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

/**
 * main - Entry point
 *
 * Return: Always 0 (Success)
 */
int main(void)
{
	int i = 0;
	pid_t pid = 0;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid < 0)
		{
			exit(EXIT_FAILURE);
		}
		else if (pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(EXIT_SUCCESS);
		}
	}
	if (pid != 0)
	{
		infinite_while();
	}
	return (0);
}
