
#!/usr/bin/python3
"""Export an employee's TODO list to a JSON file."""

import json
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user_response = requests.get(
        "{}/users/{}".format(base_url, employee_id),
        timeout=10
    )
    user_response.raise_for_status()
    user = user_response.json()

    todos_response = requests.get(
        "{}/todos".format(base_url),
        params={"userId": employee_id},
        timeout=10
    )
    todos_response.raise_for_status()
    todos = todos_response.json()

    tasks = []

    for task in todos:
        tasks.append({
            "task": task["title"],
            "completed": task["completed"],
            "username": user["username"]
        })

    data = {str(employee_id): tasks}

    filename = "{}.json".format(employee_id)

    with open(filename, "w") as jsonfile:
        json.dump(data, jsonfile, indent=4)

