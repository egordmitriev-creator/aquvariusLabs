from locust import HttpUser, task

class JSONPlaceholderTestUser(HttpUser):
    host = "https://jsonplaceholder.typicode.com"

    @task
    def posts_test(self):
        self.client.get("/posts")