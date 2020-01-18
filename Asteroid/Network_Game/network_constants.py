coordinatesOfRocket1X = []
coordinatesOfRocket1Y = []
coordinatesOfRocket2X = []
coordinatesOfRocket2Y = []

activeAsteroids = {}
bar_jedan_je_ziv_asteroid = True
asteroid_id = 0
num_of_active_asteroids = 7

player1Lives = 3
player1Hitted = 0
player2Lives = 3
player2Hitted = 0
player3Lives = 3
player3Hitted = 0
player4Lives = 3
player5Lives = 3
player6Lives = 3
player4Hitted = 0

player1Score = 0
player2Score = 0
player3Score = 0
player4Score = 0
player5Score = 0
player6Score = 0

#metkoviCoordsX = []
#metkoviCoordsY = []

bulletsCollection1X = {}
bulletsCollection1Y = {}
bulletsCollection2X = {}
bulletsCollection2Y = {}
bulletIDS = 0
bulletsCounter = 0
rocket1_bulletsCounter = 0
rocket2_bulletsCounter = 0
maximum_of_bullets = 16

level = 5   #globalna promenljiva koja odredjuje trenutni nivo
            #i na osnovu nje se kreiraju asteroidi

bonus_time = 0 #bonus dolazi na svakih 10 sekundi [5*2]
bonus_x_coordinate = 0
bonus_x_expanded = []
bonus_y_coordinate = 0
bonus_y_expanded = []

Win0 = 0 # index pobednika prvog meca
Win1 = 0 # index pobednika drugog meca
currentRound = 0 # oznacava koja je runda
                    # 0 - Player1 vs. Player2
                    # 1 - Player3 vs. Player4
                    # 2 - Win0 vs. Win1

Died = 0 # promenljiva za slucaj kad je nereseno u polufinalima, ide dalje onaj koji je druze izdrzao
Died2 = 0 # promenljiva za slucaj kad je nereseno u polufinalima, ide dalje onaj koji je druze izdrzao

tournamentActivated = False

i = 1
i2 = 1
i3 = 1
i4 = 1

is_multiplayer = False
activeBigAsteroids = []

second_player_is_here = False