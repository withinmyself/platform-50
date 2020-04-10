import tcod

from game.input import handle_keys

from functions.render_functions import render_all_entities, \
                                clear_all, render_map, game_map, \
                                player, npc, entities, con
from game.variables import *

def main():

    tcod.console_set_custom_font('arial10x10.png', tcod.FONT_TYPE_GRAYSCALE | tcod.FONT_LAYOUT_TCOD)
    tcod.console_init_root(screen_width, screen_height, 'Platform 50', False)

    keyboard_activity = tcod.Key()
    mouse_activity = tcod.Mouse()

    while not tcod.console_is_window_closed():
        tcod.sys_check_for_event(tcod.EVENT_KEY_PRESS, keyboard_activity, mouse_activity)

        render_all_entities()
        render_map()
        
        tcod.console_flush()

        clear_all()

        # We hand over the current key result into the handle_keys function
        # This function returns a library for us that we name action
        action = handle_keys(keyboard_activity)

        # We check this library for various results using the get method
        move = action.get('move')
        exit = action.get('exit')
        # power = action.get('power')
        fullscreen = action.get('fullscreen')


        # if not power:
        #     player.power = False

        if move:
            dx, dy = move # When we used get on 'move' the result is a list of two numbers (if move even happened)
            if not game_map.is_blocked(player.x + dx, player.y + dy):
                player.move(dx, dy)
            # player.x += dx
            # player.y += dy  Depending on which key we pressed the values are calculated and updated so we move in the correct direction

        # This dictionary key returns a boolean value that then says to return True which breaks the game loop.
        if exit:
            return True

        # Another boolean value which triggers a method setting fullscreen.  tcod.console_is_fullscreen() currently returns False
        # By adding not before it we change the value to True which changes the game to fullscreen.
        if fullscreen:
            tcod.console_set_fullscreen(not tcod.console_is_fullscreen())




if __name__ == '__main__':
    main()