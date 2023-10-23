#!/usr/bin/python3
"""
script that exports a csv file
"""
import csv
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

        with open(f"{argv[1]}.csv", mode="w", encoding="utf-8") as f:
            Writer = csv.writer(
                f, delimiter=",", quoting=csv.QUOTE_ALL)
            for task in tasks:
                taskStatus = task.get('completed')
                title = task.get('title')

                Writer.writerow([id, username, taskStatus, title])

    except requests.exceptions.RequestException as e:
        print(f"Error code: {e.response.status_code}")
