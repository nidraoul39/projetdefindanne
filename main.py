from uuid import *
from fastapi import *
from typing import Union
from pydantic import BaseModel
from json import *


# création du jeux
class Puissance4(BaseModel):
    grille: list = [[0 for _ in range(7)] for _ in range(6)]
    joueur0: str = None
    joueur1: str = None
    fini: bool = False
    gagnant: bool = None
    tour: bool = None

    def __init__(self, joueur1 : str, id : UUID):
        self.joueur1 = joueur1
        self.id = id
        self.status = "waiting for player 2"
        self.tour = None
        self.tours = {self.joueur0: True, self.joueur1: False}

    def join_game(self, joueur2 : str):
        self.joueur2 = joueur2
        self.status = "game is running"
    
    def play(self, joueur : int, colonne : int):
        if self.tours[joueur]:
            for i in range(6):
                if self.grille[i][colonne] == 0:
                    self.grille[i][colonne] = joueur
                    self.tours[self.joueur1] = not self.tours[self.joueur1]
                    self.tours[self.joueur2] = not self.tours[self.joueur2]
                    self.tour = joueur
                    self.check_win()
                    return True
            return False
        else:
            return False
        
    def check_win(self):
        for i in range(6):
            for j in range(7):
                if self.grille[i][j] != 0:
                    if self.grille[i][j] == self.grille[i][j+1] == self.grille[i][j+2] == self.grille[i][j+3]:
                        self.fini = True
                        self.gagnant = self.grille[i][j]
                        return True
                    if self.grille[i][j] == self.grille[i+1][j] == self.grille[i+2][j] == self.grille[i+3][j]:
                        self.fini = True
                        self.gagnant = self.grille[i][j]
                        return True
                    if self.grille[i][j] == self.grille[i+1][j+1] == self.grille[i+2][j+2] == self.grille[i+3][j+3]:
                        self.fini = True
                        self.gagnant = self.grille[i][j]
                        return True
                    if self.grille[i][j] == self.grille[i-1][j+1] == self.grille[i-2][j+2] == self.grille[i-3][j+3]:
                        self.fini = True
                        self.gagnant = self.grille[i][j]
                        return True
        return False




# création du serveur
app = FastAPI()

# status du serveur
@app.get("/")
async def root():
    return {"server status": "online"}

# liste des parties
games = []


# création d'une partie
@app.post("/create")
async def create(player1 : str):
    global games
    id = uuid4()
    games.append(id)
    return {"game id": id}


@app.get("/games")
async def get_games():
    global games
    return {"games": games}


# rejoindre une partie
@app.post("/join")
async def join_game(game_id , player2: str):
    global games
    game_id_uuid = UUID(game_id)
    if game_id_uuid in games:
        return {"game": game_id}
    else:
        return {"game": "not found"}

@app.delete("/del/")
async def del_game(game_id):
    global games
    game_id_uuid = UUID(game_id)
    if game_id_uuid in games:
        del games[games.index(game_id_uuid)]
        return {"game": game_id}
    else:
        return {"game": "not found"}
    
@app.post("/play")
async def play(game_id, player, column: int):
    global games



    game_id_uuid = UUID(game_id)
    if game_id_uuid in games:
        return {"game": game_id}
    else:
        return {"game": "not found"}
    


@app.get("/gamestatus")
async def game_status(game_id):
    global games
    game_id_uuid = UUID(game_id)
    if game_id_uuid in games:
        return {"game": game_id}
    else:
        return {"game": "not found"}
    

@app.delete("/delall")
async def del_all():
    global games
    games.clear()
    return {"games": games}