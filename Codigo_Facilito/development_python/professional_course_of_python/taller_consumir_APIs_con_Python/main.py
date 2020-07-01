import requests
#import json


if __name__ == "__main__":
    url = 'https://esc365.escardio.org/static-resources/ESC365/videoplayer/cyimplayer/2.0.7/player.html?mediaurl=https%3A%2F%2Fd381ul1ljfghfa.cloudfront.net%2FEUROCMR2019%2FScientific%2520Programme%2F186966%2FVOD%2F&signature=%3FPolicy%3DeyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vZDM4MXVsMWxqZmdoZmEuY2xvdWRmcm9udC5uZXQvRVVST0NNUjIwMTkvU2NpZW50aWZpYyUyMFByb2dyYW1tZS8xODY5NjYvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTU5MzU3NjIxOH0sIklwQWRkcmVzcyI6eyJBV1M6U291cmNlSXAiOiIwLjAuMC4wLzAifX19XX0_%26Signature%3DOswrdRoXWW2PT8fXCWYKa9%7EW1TpTrtTUL62OVMIpt1xyvl%7EovB88yPq-TL--BkzFTerXYto-naNA--rasA-CPJogeSBogDtBpdS0agU14JQ97n1EzVTI77h2q0qPL2SOVOZ7oOBhS5LDqQSd9WuSfQX1a4RnM9zXiYb7y9E0NwCa7tErRwB2R%7El8N-GOnMpigexT0-G6%7E-kX8MiESZTFXfhgwLeCmLKUKhfusCHTg2ehuXK%7EC4ENepejFfRwGoRoOpptPZkeXJ5GtVkttZG9KKPqrR-TeUsHqncXdytDtggWZcHkLx8zydqN3zLHoGkcS4EiVPHmW1aEVkt%7ELWritg__%26Key-Pair-Id%3DAPKAIWNNOMINYCK536DA&itemid=ESC365PRESENTATION186966&itemTitle=CMR+imaging+of+myocardial+fibers%3A+do+we+need+it%3F&itemEvent=EuroCMR+2019'
    response = requests.get(url, stream=True)
    with open('video.mp4', 'wb') as file:
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
