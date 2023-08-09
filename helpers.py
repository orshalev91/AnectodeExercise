import requests
import json


def check_connectivity(base_url: str, token: str) -> bool:
    # Question 2
    # Making an API GET call with end point of /user with the smallest limit of results we can ask for (5)
    # and the last page (best case - empty data, worst case - 5 results, same as other pages).
    end_point = "/user"
    headers = {"app-id": token}
    params = {"page": 999, "limit": 5}
    url = f"{base_url}{end_point}"
    try:
        dummyapi_get_call(url, headers, params)
    except Exception as error:
        print(f"Connection test failed - {error}")
        return False
    print("Connection test passed succesfully")
    return True


def dummyapi_get_call(url: str, headers: dict, params: dict):
    response = requests.get(url, headers=headers, params=params)
    if not response.ok:
        raise Exception("API Call failed")
    return response


def dump_json_file(file_name: str, data: dict) -> None:
    # Helper function, creates a json file called file_name with the data provided
    try:
        with open(file_name, "w") as fh:
            json.dump(data, fh, indent=2)
    except IOError as error:
        print(f"An error occurred while writing to the file: {error}")
