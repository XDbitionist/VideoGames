class VideoGame:
    def __init__(self, name, genre, price, popularity):
        self.name = name
        self.genre = genre
        self.price = price
        self.popularity = popularity

class VideoGameStore:
    def __init__(self):
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def get_games_by_genre(self, genre):
        return [game for game in self.games if game.genre == genre]

    def get_games_by_price(self, max_price):
        return [game for game in self.games if game.price <= max_price]

    def get_games_by_popularity(self, min_popularity):
        return [game for game in self.games if game.popularity >= min_popularity]

store = VideoGameStore()

game1 = VideoGame("The Witcher 3: Wild Hunt", "RPG", 49.99, 9.5)
game2 = VideoGame("Grand Theft Auto V", "Action", 29.99, 8.8)
game3 = VideoGame("Minecraft", "Sandbox", 26.95, 9.0)

store.add_game(game1)
store.add_game(game2)
store.add_game(game3)

rpg_games = store.get_games_by_genre("RPG")
cheap_games = store.get_games_by_price(30)
popular_games = store.get_games_by_popularity(9)

print("RPG games:")
for game in rpg_games:
    print(game.name)

print("Cheap games:")
for game in cheap_games:
    print(game.name)

print("Popular games:")
for game in popular_games:
    print(game.name)
