import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"

        response = requests.get(url)
        return response.content

    def load_json(self):
        worker_list = []
        workers = json.loads(self.get_response_body())
        for worker in workers: 
            worker_list.append(worker)

        return worker_list
        

    