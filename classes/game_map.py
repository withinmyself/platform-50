from classes.tile import Tile

class GameMap:
    """
    Methods associated with creating rooms and deciding if and when
    players, items, npcs can walk through or not.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        tiles = [[Tile(True) for y in range(self.height)] for x in range(self.width)]

        x, y = 0, 28

        for x in range(10, 60):
            tiles[x][y].blocked = True
            tiles[x][y].block_sight = True

        return tiles

    def create_room(self, room):
        # go through the tiles in the rectangle and make them passable
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.tiles[x][y].blocked = False
                self.tiles[x][y].block_sight = False

    def is_blocked(self, x, y):
        if self.tiles[x][y].blocked:
            return True

        return False