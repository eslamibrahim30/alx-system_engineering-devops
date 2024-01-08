#!/usr/bin/python3
""" This module returns information about employee's TODO list progress """
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(url + 'users/').json()
    todos = requests.get(url + 'todos/').json()
    filename = "todo_all_employees.json"
    data = {}
    for task in todos:
        currentID = task.get("userId")
        current_username = users[currentID - 1].get("username")
        task_dict = {
            "username": current_username,
            "task": task.get("title"),
            "completed": task.get("completed")
        }
        if data.get(currentID) is None:
            data[currentID] = []
        data[currentID].append(task_dict)
    json_obj = json.dumps(data)
    with open(filename, "w") as outfile:
        outfile.write(json_obj)
