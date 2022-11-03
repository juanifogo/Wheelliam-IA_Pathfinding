import requests
url = 'http://localhost:5000/test'
file = {'data': open('images/menem.jpg', 'rb')}
requests.post(url, files=file)