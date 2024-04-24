#!/usr/bin/python3
""" Using what you did in the task #0, extend your Python script to export data in the JSON format.
"""

import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    def todos(user_id):
        params={'userId': user_id}
        return requests.get(url + "todos", params=params).json()

    with open('todo_all_employees.json', 'w') as file:
        json.dump([{user['id'] : [{
            "username": user['username'],
            "task": todo['title'],
            "completed": todo['completed']} for todo in todos(user['id'])]
            for user in users}], file)
