#!/usr/bin/python3
""" This module returns information about employee's TODO list progress """
import requests
import sys


if __name__ == "__main__":
    employeeID = int(sys.argv[1])
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(employeeID)).json()
    EMPLOYEE_NAME = user.get("name")
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    DONE_TASKS = []
    todos = requests.get(url + 'todos/').json()
    for task in todos:
        if task.get("userId") == employeeID:
            TOTAL_NUMBER_OF_TASKS += 1
            if task.get("completed") is True:
                NUMBER_OF_DONE_TASKS += 1
                DONE_TASKS.append(task.get("title"))
    print("Employee {} is done with tasks".format(EMPLOYEE_NAME), end="")
    print("({}/{}):".format(NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for task in DONE_TASKS:
        print("\t {}".format(task))
