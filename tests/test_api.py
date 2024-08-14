import unittest
import requests

class APITests(unittest.TestCase):

    BASE_URL = "https://jsonplaceholder.typicode.com"

    def test_get_posts(self):
        response = requests.get(f"{self.BASE_URL}/posts")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_get_post_by_id(self):
        post_id = 1
        response = requests.get(f"{self.BASE_URL}/posts/{post_id}")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        self.assertEqual(response.json()['id'], post_id)

    def test_create_post(self):
        new_post = {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }
        response = requests.post(f"{self.BASE_URL}/posts", json=new_post)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["title"], new_post["title"])
        self.assertEqual(response.json()["body"], new_post["body"])
        self.assertEqual(response.json()["userId"], new_post["userId"])

if __name__ == "__main__":
    unittest.main()
 
