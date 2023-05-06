import requests


def get_random_users(size):
    url = f"https://random-data-api.com/api/v2/users?size={size}"

    payload = {}
    headers = {}

    users = requests.request("GET", url, headers=headers, data=payload)
    return users


