#!/usr/bin/python3
""" A python script for a given employee ID, returns
info about their TODO list progress
"""

import json
import requests
import sys


if __name__ == '__main__':
    user_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users/{}".format(user_id)).json()
    username = users.get('username', None)
    params = {"userId": "{}".format(user_id)}
    todos = requests.get(url + "todos", params=params).json()
    task_dict = {}
    value_dict = {}
    value_list = []

    for todo in todos:
        value_dict.update({'task': todo['title']})
        value_dict.update({'completed': todo['completed']})
        value_dict.update({'username': username})

        value_list.append(value_dict)
        value_dict = {}
    
    task_dict.update({users['id']: value_list})

    with open("{}.json".format(user_id), "w") as file:
        json.dump(task_dict, file)
