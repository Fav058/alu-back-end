
#!/usr/bin/python3
"""Export TODO lists for all employees to a JSON file."""

import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    users_response = requests.get(
        "{}/users".format(base_url),
        timeout=10
    )
    users_response.raise_for_status()
    users = users_response.json()

    todos_response = requests.get(
        "{}/todos".format(base_url),
        timeout=10
    )
    todos_response.raise_for_status()
    todos = todos_response.json()

    all_employees = {}

    for user in users:
        employee_id = str(user["id"])
        employee_tasks = []

        for task in todos:
            if task["userId"] == user["id"]:
                employee_tasks.append({
                    "username": user["username"],
                    "task": task["title"],
                    "completed": task["completed"]
                })

        all_employees[employee_id] = employee_tasks

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_employees, jsonfile, indent=4)

