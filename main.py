import requests

url = 'http://127.0.0.1:8080/api/members/ex'
#여기에 헤더 입력
headers = {
    'Accept' : 'application/json'
}

response = requests.get(url, headers=headers)


print(f'status code : {response.status_code}')
print('response body : ')
print(response.text)