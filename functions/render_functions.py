import tcod

def render_map(con, entities, game_map, colors):
   # Draw all the tiles in the game map
    for y in range(game_map.height):
        for x in range(game_map.width):
            wall = game_map.tiles[x][y].block_sight

            if wall:
                tcod.console_set_char_background(con, x, y, colors.get('dark_wall'), tcod.BKGND_SET)
            else:
                tcod.console_set_char_background(con, x, y, colors.get('dark_ground'), tcod.BKGND_SET)


def render_all_entities(con, entities, screen_width, screen_height):
    
    # Draw all entities in the list
    for entity in entities:
        draw_entity(con, entity)

        if entity.player:
            draw_entity_part(con, entity.x - 1, entity.y, '[', tcod.orange)
            draw_entity_part(con, entity.x + 1, entity.y, ']', tcod.orange)
            draw_entity_part(con, entity.x - 2, entity.y, '[', tcod.red)
            draw_entity_part(con, entity.x + 2, entity.y, ']', tcod.orange)
            draw_entity_part(con, entity.x - 3, entity.y, ':', tcod.orange)
            draw_entity_part(con, entity.x + 3, entity.y, ':', tcod.white)
            draw_entity_part(con, entity.x - 1, entity.y + 1, '|', tcod.orange)
            draw_entity_part(con, entity.x + 1, entity.y + 1, '|', tcod.orange)

    tcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)


def clear_all(con, entities):
    for entity in entities:
        clear_entity(con, entity)

        if entity.player:
            clear_entity_part(con, entity.x - 1, entity.y)
            clear_entity_part(con, entity.x + 1, entity.y)
            clear_entity_part(con, entity.x - 2, entity.y)
            clear_entity_part(con, entity.x + 2, entity.y)
            clear_entity_part(con, entity.x - 3, entity.y)
            clear_entity_part(con, entity.x + 3, entity.y)
            clear_entity_part(con, entity.x - 1, entity.y + 1)
            clear_entity_part(con, entity.x + 1, entity.y + 1)


def draw_entity(con, entity):
    tcod.console_set_default_foreground(con, entity.color)
    tcod.console_put_char(con, entity.x, entity.y, entity.char, tcod.BKGND_NONE)

def draw_entity_part(con, alt_x, alt_y, entity_part, part_color):
    tcod.console_set_default_foreground(con, part_color)
    tcod.console_put_char(con, alt_x, alt_y, entity_part, tcod.BKGND_NONE)


def clear_entity(con, entity):
    # erase the character that represents this object
    tcod.console_put_char(con, entity.x, entity.y, ' ', tcod.BKGND_NONE)

def clear_entity_part(con, alt_x, alt_y):
    # erase the character that represents this object
    tcod.console_put_char(con, alt_x, alt_y, ' ', tcod.BKGND_NONE)