import requests

r = requests.get('https://httpbin.org/get')
print(r.status_code)
print(r.json())
print(r.json()['url'])

payload = {"course": "CBF - Python", "level": "Beginner"}
r_post = requests.post('https://httpbin.org/post', json=payload)
print(r_post.json()["json"])