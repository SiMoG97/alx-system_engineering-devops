#!/usr/bin/python3
"""
script that exports a csv file
"""
import json
import requests


if __name__ == "__main__":
    try:
        usersRes = requests.get(
            "https://jsonplaceholder.typicode.com/users")

        usersRes.raise_for_status()

        users = usersRes.json()
        usersObj = {}
        for user in users:
            id = user.get('id')
            tasksRes = requests.get(
                f"https://jsonplaceholder.typicode.com/todos?userId={id}")
            tasksRes.raise_for_status()

            username = user.get('username')
            tasks = tasksRes.json()
            userTasks = []
            for task in tasks:
                obj = {
                    'task': task.get('title'),
                    'completed': task.get('completed'),
                    'username': username
                }
                userTasks.append(obj)

            usersObj[id] = userTasks

        with open("todo_all_employees.json", mode="w", encoding="utf-8") as f:
            f.write(json.dumps(usersObj))

    except requests.exceptions.RequestException as e:
        print(f"Error code: {e.response.status_code}")
