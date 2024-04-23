#!/usr/bin/python3
""" A python script for a given employee ID, returns
info about their TODO list progress
"""

import csv
import requests
import sys


if __name__ == '__main__':
    user_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get('username', None)
    params = {"userId": "{}".format(user_id)}
    todos = requests.get(url + "todos", params=params).json()

    with open("{}.csv".format(user_id), "w", newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]
