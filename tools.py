import json
import os
import random

def generate_users(names, age_range=(20, 30), domain="gmail.com"):
    users = []

    for name in names:
        users.append({
            "name": name,
            "email": f"{name.lower()}@{domain}",
            "age": random.randint(age_range[0], age_range[1])
        })

    return users


def save_users(users):
    os.makedirs("outputs", exist_ok=True)

    path = "outputs/users.json"
    with open(path, "w") as f:
        json.dump(users, f, indent=4)

    return path