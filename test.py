from main import *
from pathlib import Path
import unittest


class TestExercise(unittest.TestCase):
    # Testing connectivity test with valid and invalid tokens
    def test_connection(self):
        # Valid token
        self.assertTrue(
            check_connectivity(
                "https://dummyapi.io/data/v1/", "64cfb043fdcad132819bd09b"
            )
        )
        # Invalid token
        self.assertFalse(
            check_connectivity("https://dummyapi.io/data/v1/", "invalid_token")
        )

    # Testing UserEvidence class with both valid and invalid tokens.
    # For valid token we expect to contain a key "data" and the value of "data" to be a none empty list.
    # For the invalid token we expect the result to be None
    def test_user_list_valid_token(self):
        evidence = UserEvidence()
        evidence_result = evidence.fetch_evidence()
        self.assertIn("data", evidence_result)
        self.assertIsInstance(evidence_result.get("data"), list)
        self.assertIsNotNone(evidence_result.get("data"))

    def test_user_list_invalid_token(self):
        evidence = UserEvidence()
        print("invalid token user")
        evidence.token = "Invalid_token"
        evidence_result = evidence.fetch_evidence()
        self.assertEqual(evidence_result, None)

    # Testing get_posts function with both valid and invalid tokens.
    # For valid token we expect the result to contain "data" field, and to have a none empty list in it.
    # For the invalid token we expect the results to be None
    def test_post_list_valid_token(self):
        evidence = PostEvidence()
        evidence_result = evidence.fetch_evidence()
        self.assertIn("data", evidence_result)
        self.assertIsInstance(evidence_result.get("data"), list)
        self.assertIsNotNone(evidence_result.get("data"))

    def test_post_list_invalid_token(self):
        evidence = PostEvidence()
        print("invalid token user")
        evidence.token = "Invalid_token"
        evidence_result = evidence.fetch_evidence()
        self.assertEqual(evidence_result, None)

    # Testing get_post_comment helper function with valid and invalid post ID.
    def test_get_post_comment(self):
        evidence = PostEvidence()
        self.assertIsInstance(
            evidence._PostEvidence__get_post_comment("60d21afc67d0d8992e610baa"), list
        )
        self.assertNotEqual(
            evidence._PostEvidence__get_post_comment("60d21afc67d0d8992e610baa"), []
        )
        # Invalid post id
        self.assertEqual(evidence._PostEvidence__get_post_comment("Invalid_Id"), [])

    # Testing dump_json_file helper function creates a file
    def test_dump_json_file(self):
        my_dict = {"name": "John"}
        dump_json_file("test_file", my_dict)
        file_obj = Path("test_file")
        self.assertTrue(file_obj.exists())
        file_obj.unlink()
