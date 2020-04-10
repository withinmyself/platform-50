class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """
    def __init__(self, x, y, char, color, player=True, power=True):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.player = player
        self.power = power

    def move(self, dx, dy):
        # Move the entity by a given amount
        self.x += dx
        self.y += dy