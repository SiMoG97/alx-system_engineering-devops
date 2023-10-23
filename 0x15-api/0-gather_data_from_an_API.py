#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
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

        name = user['name']

        userRes.raise_for_status()
        tasksRes.raise_for_status()

        tasksLen = len(tasks)
        completedTasks = [task for task in tasks if task['completed']]
        doneTasksNum = len(completedTasks)

        print(
            f"Employee {name} is done with tasks({doneTasksNum}/{tasksLen}):")
        for task in completedTasks:
            print(f"\t {task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error code: {e.response.status_code}")
