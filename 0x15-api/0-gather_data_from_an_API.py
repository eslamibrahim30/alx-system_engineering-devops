#!/usr/bin/python3
import requests
import sys
if __name__ == "__main__":
    employeeID = int(sys.argv[1])
    users = requests.get('https://jsonplaceholder.typicode.com/users/').json()
    for user in users:
        if user.get("id") == employeeID:
            EMPLOYEE_NAME = user.get("name")
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    UNDONE_TASKS = []
    todos = requests.get('https://jsonplaceholder.typicode.com/todos/').json()
    for task in todos:
        if task.get("userId") == employeeID:
            TOTAL_NUMBER_OF_TASKS += 1
            if task.get("completed") is True:
                NUMBER_OF_DONE_TASKS += 1
            else:
                UNDONE_TASKS.append(task.get("title"))
    print("Employee {} is done with tasks".format(EMPLOYEE_NAME), end="")
    print("({}/{}):".format(NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for task in UNDONE_TASKS:
        print("\t{}".format(task))
