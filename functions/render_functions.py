import tcod

from static.blueprints import \
    build_light_walker, destroy_light_walker, build_lw_cell_2, \
    destroy_lw_cell_2, build_lw_cell_3, build_lw_cell_4, \
    build_lw_cell_5, build_lw_cell_6, build_lw_cell_7
from static.variables import *

from classes.entity import Entity
from classes.game_map import GameMap
from classes.map_shapes import Rect

colors = {
'dark_wall' : tcod.Color(100, 0, 0),
'dark_ground' : tcod.Color(50, 50, 150)
}
con = tcod.console_new(screen_width, screen_height)
game_map = GameMap(map_width, map_height)
player = Entity(int(screen_width / 2), int(screen_height / 2), '@', tcod.white, player=True)
npc = Entity(int(screen_width / 2), int(screen_height / 2), ' ', tcod.white, player=False)
entities = [player]
room = Rect(player.x - 15, player.y - 15, 15, 15)

def render_map():
   # Draw all the tiles in the game map
    for y in range(game_map.height):
        for x in range(game_map.width):
            wall = game_map.tiles[x][y].block_sight

            if wall:
                tcod.console_set_char_background(con, x, y, colors.get('dark_wall'), tcod.BKGND_SET)
            else:
                tcod.console_set_char_background(con, x, y, colors.get('dark_ground'), tcod.BKGND_SET)

def render_room():
    game_map.create_room(room)

def render_all_entities():
    # Draw all entities in the list
    for entity in entities:
        draw_entity(con, entity)

    tcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)

def clear_all():
    for entity in entities:
        clear_entity(con, entity)

        if entity.player:
            destroy_light_walker(con, entity)

def draw_entity(con, entity):
    tcod.console_set_default_foreground(con, entity.color)
    tcod.console_put_char(con, entity.x, entity.y, entity.char, tcod.BKGND_NONE)

def clear_entity(con, entity):
    tcod.console_put_char(con, entity.x, entity.y, ' ', tcod.BKGND_NONE)

