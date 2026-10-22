
#!/usr/bin/python3
"""Export an employee's TODO list to a CSV file."""

import csv
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

    filename = "{}.csv".format(employee_id)

    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                user["username"],
                task["completed"],
                task["title"]
            ])

