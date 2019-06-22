from locust import HttpLocust, TaskSet, task
import random as rnd


class UserBehavior(TaskSet):
    @task(1)
    def check_albums(self):
        photo_id = rnd.randint(1, 5000)
        with self.client.get('/1/{id}', catch_response=True, name='/1/[id]') as response:
            if response.status_code == 200:
                album_id = response.json().get('Id')
                if album_id % 10 != 0:
                    response.success()
                else:
                    response.failure('id cannot be {id}')
            else:
                response.failure('status code is {response.status_code}')


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 2000
