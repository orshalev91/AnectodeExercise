from evidences.base_evidence import Evidence
from helpers import dummyapi_get_call


class UserEvidence(Evidence):
    name = "users"

    def fetch_evidence(self):
        return self.__get_users_list()

    def __get_users_list(self) -> dict:
        # Question 3
        # The function will start from page 0 and continue until the data it receives is empty.
        # all the users data will be collected in "all_data" var and will be converted into dictionary
        # and will be saved in json file called "users.json"
        print("Fetching Users")
        end_point = "/user"
        page = 0
        limit = 50
        all_data = []
        headers = {"app-id": self.token}
        params = {"page": page, "limit": limit}
        url = f"{super().base_url}{end_point}"

        while True:
            params["page"] = page
            try:
                response = dummyapi_get_call(url, headers, params)
                result = response.json()
                users = result.get("data")
                all_data.extend(users)
                total_users = int(result.get("total"))
                page += 1
                if limit * page >= total_users:
                    break
            except Exception as error:
                print(error)
                return None

        return {"data": all_data}
