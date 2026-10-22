#!/usr/bin/python3
"""Gather an employee's completed TODO tasks from an API."""

import sys
import requests


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    user_url = (
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    )
    todos_url = (
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            employee_id
        )
    )

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_response.raise_for_status()
    todos_response.raise_for_status()

    user = user_response.json()
    todos = todos_response.json()

    completed_tasks = [task for task in todos if task["completed"]]

    print(
        "Employee {} is done with tasks({}/{}):".format(
            user["name"], len(completed_tasks), len(todos)
        )
    )

    for task in completed_tasks:
        print("\t {}".format(task["title"]))
