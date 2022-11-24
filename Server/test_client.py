import requests
url = 'http://localhost:5000/test' #ip:puerto/carpeta
file = {'data': open('images/menem.jpg', 'rb')}
requests.post(url, files=file)