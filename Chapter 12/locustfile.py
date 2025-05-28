from locust import HttpUser, task

class LoadTestDemo (HttpUser):
    @task
    def root_request(self):
        self.client.get("/")
