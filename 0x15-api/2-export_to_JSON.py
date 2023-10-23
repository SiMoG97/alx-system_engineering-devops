#!/usr/bin/python3
"""
script that exports a csv file
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    try:
        userRes = requests.get(
            f"https://jsonplaceholder.typicode.com/users/{argv[1]}")
        tasksRes = requests.get(
            f"https://jsonplaceholder.typicode.com/todos?userId={argv[1]}")

        user = userRes.json()
        tasks = tasksRes.json()

        userRes.raise_for_status()
        tasksRes.raise_for_status()

        id = user.get('id')
        username = user.get('username')

        userObj = {}
        userTasks = []
        for task in tasks:
            obj = {
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': username
            }
            userTasks.append(obj)

        userObj[id] = userTasks

        with open(f"{argv[1]}.json", mode="w", encoding="utf-8") as f:
            f.write(json.dumps(userObj))

    except requests.exceptions.RequestException as e:
        print(f"Error code: {e.response.status_code}")
