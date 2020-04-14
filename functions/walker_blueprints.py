import tcod
from game.entity import Entity
import time



def draw_entity_part(con, alt_x, alt_y, entity_part, part_color):
    tcod.console_set_default_foreground(con, part_color)
    tcod.console_put_char(con, alt_x, alt_y, entity_part, tcod.BKGND_NONE)

def clear_entity_part(con, alt_x, alt_y):
    # erase the character that represents this object
    # by replacing the char with an empty space
    tcod.console_put_char(con, alt_x, alt_y, ' ', tcod.BKGND_NONE)


# __________
# Light Walker
#
#    :((@)):
#      | |
#      | |
# __________
#
# Coordinates:
# (, ), (, ), :, :, |, |, |, |
# x: -1, +1, -2, +2, -3, +3, -1, +1, -1, +1
# y: 0, 0, 0, 0, 0, 0, +1, +1, +2, +2
def build_light_walker(con, entity):
    x = (-1, +1, -2, +2, -3, +3, -1, +1, -1, +1)
    y = (0, 0, 0, 0, 0, 0, +1, +1, +2, +2)
    characters = ('(', ')', '(', ')', ':', ':', '|', '|', '|', '|')
    colors = (tcod.grey, tcod.grey, tcod.black, tcod.black, tcod.red, tcod.red, tcod.grey, tcod.grey, tcod.grey, tcod.grey)
    for i in range(0,10):
        draw_entity_part(con, entity.x + x[i], entity.y + y[i], characters[i], colors[i])


def build_lw_cell_2(con, entity):
    x = (-2, +2, -3, +3, -4, +4, -1, +1, -1, +1, 0)
    y = ( 0, 0, 0, 0, 0, 0, +1, +1, +2, +2, +1)
    characters = ('(', ')', '(', ')', ':', ':', '|', '|', '|', '|', '=')
    colors = (tcod.grey, tcod.grey, tcod.black, tcod.black, tcod.red, tcod.red, tcod.grey, tcod.grey, tcod.grey, tcod.grey, tcod.grey)
    for i in range(0,11):
        draw_entity_part(con, entity.x + x[i], entity.y + y[i], characters[i], colors[i])

    # draw_entity_part(con, entity.x - 2, entity.y, '(', tcod.grey)
    # draw_entity_part(con, entity.x + 2, entity.y, ')', tcod.grey)
    # draw_entity_part(con, entity.x - 3, entity.y, '(', tcod.black)
    # draw_entity_part(con, entity.x + 3, entity.y, ')', tcod.black)
    # draw_entity_part(con, entity.x - 4, entity.y, ':', tcod.red)
    # draw_entity_part(con, entity.x + 4, entity.y, ':', tcod.red)
    # draw_entity_part(con, entity.x - 1, entity.y + 1, '|', tcod.grey)
    # draw_entity_part(con, entity.x + 1, entity.y + 1, '|', tcod.grey)
    # draw_entity_part(con, entity.x - 1, entity.y + 2, '|', tcod.grey)
    # draw_entity_part(con, entity.x + 1, entity.y + 2, '|', tcod.grey)
    # draw_entity_part(con, entity.x , entity.y + 1, '=', tcod.grey)

def build_lw_cell_3(con, entity):
    draw_entity_part(con, entity.x - 2, entity.y, '(', tcod.grey)
    draw_entity_part(con, entity.x + 2, entity.y, ')', tcod.grey)
    draw_entity_part(con, entity.x - 3, entity.y, '(', tcod.black)
    draw_entity_part(con, entity.x + 3, entity.y, ')', tcod.black)
    draw_entity_part(con, entity.x - 4, entity.y, ':', tcod.red)
    draw_entity_part(con, entity.x + 4, entity.y, ':', tcod.red)
    draw_entity_part(con, entity.x - 2, entity.y + 1, '|', tcod.grey)
    draw_entity_part(con, entity.x + 2, entity.y + 1, '|', tcod.grey)
    draw_entity_part(con, entity.x - 1, entity.y + 2, '|', tcod.grey)
    draw_entity_part(con, entity.x + 1, entity.y + 2, '|', tcod.grey)
    draw_entity_part(con, entity.x , entity.y + 1, '=', tcod.grey)
    draw_entity_part(con, entity.x , entity.y + 2, '=', tcod.grey)





def destroy_lw_cell_2(con, entity):
    x = (-2, +2, -3, +3, -4, +4, -1, +1, -1, +1, 0)
    y = (0, 0, 0, 0, 0, 0, +1, +1, +2, +2, +1)
    for i in x:
        for j in y:
            clear_entity_part(
                con, entity.x + i, entity.y + j )

def destroy_light_walker(con, entity):
    x = (-1, +1, -2, +2, -3, +3, -1, +1, -1, +1)
    y = (0, 0, 0, 0, 0, 0, +1, +1, +2, +2)
    for i in range(0,10):
        clear_entity_part(con, entity.x + x[i], entity.y + y[i])
