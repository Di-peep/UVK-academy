import requests


class Client:
    def __init__(self, link: str):
        self.link = link

    def get(self):
        response = requests.get(self.link)
        print(f'Get request: {response.text}')

    def post(self, data: dict):
        response = requests.post(self.link, json=data)
        print(f'Post request: status code {response.status_code}')


if __name__ == '__main__':
    client = Client('http://localhost:9595')
    client.get()
    client.post({"name": "Abc", "age": "20"})
    client.get()
