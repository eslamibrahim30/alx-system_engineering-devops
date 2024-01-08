#!/usr/bin/python3
""" This module returns information about employee's TODO list progress """
import json
import requests
import sys


if __name__ == "__main__":
    employeeID = int(sys.argv[1])
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(employeeID)).json()
    todos = requests.get(url + 'todos/').json()
    username = user.get("username")
    filename = "{}.json".format(employeeID)
    data = []
    for task in todos:
        if task.get("userId") == employeeID:
            task_dict = {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": username
            }
            data.append(task_dict)
    print(data)
    json_obj = json.dumps({employeeID: data})
    with open(filename, "w") as outfile:
        outfile.write(json_obj)
