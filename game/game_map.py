from game.tile import Tile



class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        tiles = [[Tile(False) for y in range(self.height)] for x in range(self.width)]

        x, y = 0, 22

        for x in range(10, 60):
            tiles[x][y].blocked = True
            tiles[x][y].block_sight = True



        return tiles

    def is_blocked(self, x, y):
        if self.tiles[x][y].blocked:
            return True

        return False