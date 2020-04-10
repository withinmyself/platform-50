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
        self.cell_1 = False
        self.cell_2 = False
        self.cell_3 = False

    def move(self, dx, dy):
        # Move the entity by a given amount
        self.x += dx
        self.y += dy

    def change_cell(self, current, new):
        if current == 1:
            self.cell_1 = False
            self.cell_2 = True
        elif current == 2:
            self.cell_2 = False
            self.cell_3 = True
        elif current == 3:
            self.cell_3 = False
            self.cell_2 = True
        elif current == 0:
            self.cell_3, self.cell_2 = False, False
            self.cell_1 = True
        else:
            print("Invalid Context when attempting to change cell animation.  Line 34 - Entity.py")


    