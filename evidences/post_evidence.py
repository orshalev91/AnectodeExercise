from evidences.base_evidence import Evidence
from helpers import dummyapi_get_call


class PostEvidence(Evidence):
    name = "posts"

    def fetch_evidence(self):
        return self.__get_posts()

    def __get_posts(self) -> dict:
        # Question 4
        # The function will get 50 posts, for each post we will use a get API call for its comments and create a "comment" field
        # for the post with the received value.
        # The posts with the comments will be returned as a dictionary
        # and will be saved in json file called "posts.json"
        print("Fetching Posts")
        end_point = "/post"
        headers = {"app-id": self.token}
        params = {"page": 0, "limit": 50}
        url = f"{super().base_url}{end_point}"

        try:
            response = dummyapi_get_call(url, headers, params)
            results = response.json()
            posts = results.get("data")
            for post in posts:
                post_id = post["id"]
                comments = self.__get_post_comment(post_id)
                post["comments"] = comments
        except Exception as error:
            print(error)
            return None

        return {"data": posts}

    def __get_post_comment(self, id: str) -> list:
        # Question 4 helper function
        # getting the first 50 comments that were created for a specific post.
        # pagination wasn't mentioned regarding comments so my assumption is there are no more than 50 comments for each post.
        print(f"Fetching comments for post id: {id}")
        end_point = f"/post/{id}/comment"
        headers = {"app-id": self.token}
        params = {"page": 0, "limit": 50}
        url = f"{super().base_url}{end_point}"
        try:
            response = dummyapi_get_call(url, headers, params)
            results = response.json()
            comments = results.get("data")
        except Exception as error:
            print(error)
            # Return empty list instead of aborting to try and recover from bad api call
            return []

        return comments
