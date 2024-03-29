#!/usr/bin/python3
""" This module returns information about employee's TODO list progress """
import csv
import requests
import sys


if __name__ == "__main__":
    employeeID = int(sys.argv[1])
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(employeeID)).json()
    todos = requests.get(url + 'todos/').json()
    username = user.get("username")
    filename = "{}.csv".format(employeeID)
    f = open(filename, 'w')
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    for task in todos:
        if task.get("userId") == employeeID:
            row = [
                    employeeID,
                    username,
                    task.get("completed"),
                    task.get("title")
            ]
            writer.writerow(row)
