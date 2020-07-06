import requests
#import json


if __name__ == "__main__":
    url = 'https://www.goodfreephotos.com/albums/maldives/resort-beach-and-ocean-landscape-in-the-maldives.jpg'
    response = requests.get(url, stream=True)
    with open('pic.png', 'wb') as file:
        for chunk in response.iter_content():
            file.write(chunk)
    
    response.close()


""" if __name__ == "__main__":
    url = 'http://httpbin.org/delete'
    payload = { 'name': 'Juan', 'last_name': 'Restrepo', 'age': 41 }
    headers = { 'Conten-Type' : 'applicationes/json', 'token' : '12345' }

    response = requests.put(url, data=json.dumps(payload), headers=headers)
    response = requests.delete(url, data=json.dumps(payload), headers=headers)
    print(response.url)

    if response.status_code == 200:
        print(response.content) # imprime json
        headers_response = response.headers
        server = headers_response['Server']
        print(server) """

""" if __name__ == "__main__":
    url = 'http://httpbin.org/post'
    payload = { 'name': 'Juan', 'last_name': 'Restrepo', 'age': 41 }
    headers = { 'Conten-Type' : 'applicationes/json', 'token' : '12345' }

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response.url)

    if response.status_code == 200:
        print(response.content) # imprime json
        headers_response = response.headers
        server = headers_response['Server']
        print(server) """

""" if __name__ == "__main__":
    url = 'http://httpbin.org/post'
    payload = { 'name': 'Juan', 'last_name': 'Restrepo', 'age': 41 }

    response = requests.post(url, json=payload) # json post se encarga de serializar
    response = requests.post(url, data=payload) # Los mando dentro de form
    response = requests.post(url, data=json.dumps(payload)) # data post hay que hacerlo nosotros la serializacion
    print(response.url)

    if response.status_code == 200:
        print(response.content) # imprime json  """

""" if __name__ == "__main__":
    url = 'http://httpbin.org/get'
    args = { 'name': 'Juan', 'last_name': 'Restrepo', 'age': 41 }
    
    response = requests.get(url, params=args)
    #print(response)
    #print(response.url)

    if response.status_code == 200:
        text = response.text #Python: json ordering Python3: json ordering
        content = response.content #Python: json ordering Python3: b \n json
        response_json = response.json() #Python: u{} Python3: json oneline
        print(content)



        content = response.content
        print(content)
        response_json = json.loads(response.text)
        origin = response_json['orgin']
        print(origin)

        response_json = response.json()
        origin = response_json['origin']
        print(origin) """


""" if __name__ == "__main__":
    url = 'http://httpbin.org/get'
    args = { 'name': 'Juan', 'last_name': 'Restrepo', 'age': 41 }
    
    response = requests.get(url, params=args)
    print(response.url)

    if response.status_code == 200:
        content = response.content
        print(content)

print(response) """
