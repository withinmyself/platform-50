import tcod
from game.entity import Entity


def draw_entity_part(con, alt_x, alt_y, entity_part, part_color):
    tcod.console_set_default_foreground(con, part_color)
    tcod.console_put_char(con, alt_x, alt_y, entity_part, tcod.BKGND_NONE)

def clear_entity_part(con, alt_x, alt_y):
    # erase the character that represents this object
    # by replacing the char with an empty space
    tcod.console_put_char(con, alt_x, alt_y, ' ', tcod.BKGND_NONE)

def build_light_runner(con, entity):
    draw_entity_part(con, entity.x - 1, entity.y, '(', tcod.grey)
    draw_entity_part(con, entity.x + 1, entity.y, ')', tcod.grey)
    draw_entity_part(con, entity.x - 2, entity.y, '(', tcod.black)
    draw_entity_part(con, entity.x + 2, entity.y, ')', tcod.black)
    draw_entity_part(con, entity.x - 3, entity.y, ':', tcod.red)
    draw_entity_part(con, entity.x + 3, entity.y, ':', tcod.red)
    draw_entity_part(con, entity.x - 1, entity.y + 1, '|', tcod.grey)
    draw_entity_part(con, entity.x + 1, entity.y + 1, '|', tcod.grey)
    draw_entity_part(con, entity.x - 1, entity.y + 2, '|', tcod.grey)
    draw_entity_part(con, entity.x + 1, entity.y + 2, '|', tcod.grey)

def build_lw_cell_2(con, entity):
    draw_entity_part(con, entity.x - 2, entity.y, '(', tcod.grey)
    draw_entity_part(con, entity.x + 2, entity.y, ')', tcod.grey)
    draw_entity_part(con, entity.x - 3, entity.y, '(', tcod.black)
    draw_entity_part(con, entity.x + 3, entity.y, ')', tcod.black)
    draw_entity_part(con, entity.x - 4, entity.y, ':', tcod.red)
    draw_entity_part(con, entity.x + 4, entity.y, ':', tcod.red)
    draw_entity_part(con, entity.x - 1, entity.y + 1, '|', tcod.grey)
    draw_entity_part(con, entity.x + 1, entity.y + 1, '|', tcod.grey)
    draw_entity_part(con, entity.x - 1, entity.y + 2, '|', tcod.grey)
    draw_entity_part(con, entity.x + 1, entity.y + 2, '|', tcod.grey)
    draw_entity_part(con, entity.x , entity.y + 1, '=', tcod.grey)





def destroy_lw_cell_2(con, entity):
    clear_entity_part(con, entity.x - 2, entity.y)
    clear_entity_part(con, entity.x + 2, entity.y)
    clear_entity_part(con, entity.x - 3, entity.y)
    clear_entity_part(con, entity.x + 3, entity.y)
    clear_entity_part(con, entity.x - 4, entity.y)
    clear_entity_part(con, entity.x + 4, entity.y)
    clear_entity_part(con, entity.x - 1, entity.y + 1)
    clear_entity_part(con, entity.x + 1, entity.y + 1)
    clear_entity_part(con, entity.x - 1, entity.y + 2)
    clear_entity_part(con, entity.x + 1, entity.y + 2)
    clear_entity_part(con, entity.x, entity.y + 1)





def destroy_light_runner(con, entity):
    clear_entity_part(con, entity.x - 1, entity.y)
    clear_entity_part(con, entity.x + 1, entity.y)
    clear_entity_part(con, entity.x - 2, entity.y)
    clear_entity_part(con, entity.x + 2, entity.y)
    clear_entity_part(con, entity.x - 3, entity.y)
    clear_entity_part(con, entity.x + 3, entity.y)
    clear_entity_part(con, entity.x - 1, entity.y + 1)
    clear_entity_part(con, entity.x + 1, entity.y + 1)
    clear_entity_part(con, entity.x - 1, entity.y + 2)
    clear_entity_part(con, entity.x + 1, entity.y + 2)

