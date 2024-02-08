import requests
import json

class Client():
    def __init__(self, url: str):
        self.session = requests.Session()
        self.url = url
        

    def get(self):
        url = self.url
        return self.session.get(url)

    def post(self, ur,data):
        url = self.url + ur + "?"+ data
        print(url)
        return self.session.post(url)
    
    def delete(self,data):
        url = self.url + data
        return self.session.delete(url)


    

cl  = Client('http://localhost:8000')

t = cl.get().text

print(cl.post('/create','player1=dani').text)
id = None

if id != None:
    gameid= "/game_id?="+ id
    print(cl.delete(gameid).text)

