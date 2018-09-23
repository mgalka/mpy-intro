# urequests module needs to be installed beforehand
import urequests

url = 'http://jsonplaceholder.typicode.com/posts'
data = {
    'userId': 1,
    'topic': 'Test post',
    'body': 'Sample body'
}
resp = urequests.post(url, json=data)

print(resp.json())