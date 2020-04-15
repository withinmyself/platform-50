import tcod

import time

from functions.walker_blueprints import build_light_walker, destroy_light_walker, \
                                        build_lw_cell_2, destroy_lw_cell_2, \
                                        build_lw_cell_3, build_lw_cell_4, \
                                        build_lw_cell_5, build_lw_cell_6, \
                                        build_lw_cell_7

from game.entity import Entity
from game.variables import *
from game.game_map import GameMap


colors = {
'dark_wall' : tcod.Color(100, 0, 0),
'dark_ground' : tcod.Color(50, 50, 150)
}
# npc = True
con = tcod.console_new(screen_width, screen_height)
game_map = GameMap(map_width, map_height)
player = Entity(int(screen_width / 2), int(screen_height / 2), '@', tcod.white, player=True)
npc = Entity(int(screen_width / 2), int(screen_height / 2), ' ', tcod.white, player=False)
entities = [player]
# if npc:
#     npc = Entity(player.x, player.y, ' ', tcod.yellow, player=False)
#     entities = [player, npc]
# else:
#     entities = [player]





def render_map():
   # Draw all the tiles in the game map
    for y in range(game_map.height):
        for x in range(game_map.width):
            wall = game_map.tiles[x][y].block_sight

            if wall:
                tcod.console_set_char_background(con, x, y, colors.get('dark_wall'), tcod.BKGND_SET)
            else:
                tcod.console_set_char_background(con, x, y, colors.get('dark_ground'), tcod.BKGND_SET)

# def render_walker_animation(entering):
#     if entering:

#     else:


def render_mech_animation():
    build_light_walker(con, player)
    destroy_light_walker(con, player)
    build_lw_cell_2(con, player)
    build_lw_cell_3(con, player)
    build_lw_cell_4(con, player)
    build_lw_cell_5(con, player)
    build_lw_cell_6(con, player)
    tcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)



def render_all_entities():
    # Draw all entities in the list
    for entity in entities:
        draw_entity(con, entity)


    tcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)
    # Console_blit is bringing forth our new console as the default viewable console.
    # tcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)

def clear_all():
    for entity in entities:
        clear_entity(con, entity)

        if entity.player:
            destroy_light_walker(con, entity)





def draw_entity(con, entity):
    tcod.console_set_default_foreground(con, entity.color)
    tcod.console_put_char(con, entity.x, entity.y, entity.char, tcod.BKGND_NONE)

def clear_entity(con, entity):
    # erase the character that represents this object
    tcod.console_put_char(con, entity.x, entity.y, ' ', tcod.BKGND_NONE)

