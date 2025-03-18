from locust import HttpUser, task

class WttrTestUser(HttpUser):
    host = "https://wttr.in"

    @task
    def wethter_test(self):
        self.client.get("/Novosibirsk?format=j1")