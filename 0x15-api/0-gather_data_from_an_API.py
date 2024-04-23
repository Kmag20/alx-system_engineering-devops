#!/usr/bin/python3
""" A python script for a given employee ID, returns
info about their TODO list progress
"""

import sys
import requests

if __name__ == '__main__':
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users/{}".format(user_id)).json()
    params = {"userId": "{}".format(user_id)}
    todos = requests.get(url + "todos", params=params).json()
    completed_tasks = sum(1 for todo in todos if todo['completed'])
    print("Employee {} is done with tasks ({}/{}):".format(users['name'],
          completed_tasks, len(todos)))
    for todo in todos:
        if todo['completed'] is True:
            print("\t{}".format(todo['title']))
