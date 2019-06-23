from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):

    @task(1)
    def on_start(self):
        self.client.get("/")

    @task(2)
    def posts(self):
        self.client.head("/")

    @task(3)
    def on_start(self):
        self.client.get("/delivery")

    @task(4)
    def posts(self):
        self.client.head("/")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 2000
