import tcod

import time

from game.input import handle_keys

from functions.render_functions import render_all_entities, \
                                clear_all, render_map, game_map, \
                                player, entities, con, npc, render_mech_animation
from functions.walker_blueprints import *
from game.variables import *

def main():

    tcod.console_set_custom_font('arial10x10.png', tcod.FONT_TYPE_GRAYSCALE | tcod.FONT_LAYOUT_TCOD)
    tcod.console_init_root(screen_width, screen_height, 'Platform 50', False)

    keyboard_activity = tcod.Key()
    mouse_activity = tcod.Mouse()
    build = True
    solo = True

    while not tcod.console_is_window_closed():
        tcod.sys_check_for_event(tcod.EVENT_KEY_PRESS, keyboard_activity, mouse_activity)

        if solo:
            render_map()
            render_all_entities()
            build_light_walker(con, npc)
            destroy_light_walker(con, player)
            tcod.console_flush()
            clear_all()

        elif build and not solo:
            render_map()
            render_all_entities()
            build_light_walker(con, player)
            time.sleep(3)
            destroy_light_walker(con, player)
            tcod.console_flush()
            clear_all()

            render_map()
            render_all_entities()
            build_lw_cell_2(con, player)
            time.sleep(0.2)
            destroy_lw_cell_2(con, player)
            tcod.console_flush()
            clear_all()
            
            render_map()
            render_all_entities()
            build_lw_cell_3(con, player)
            time.sleep(0.2)
            destroy_lw_cell_3(con, player)
            tcod.console_flush()
            clear_all()

            render_map()
            render_all_entities()
            build_lw_cell_4(con, player)
            time.sleep(0.2)
            destroy_lw_cell_4(con, player)
            tcod.console_flush()
            clear_all()

            render_map()
            render_all_entities()
            build_lw_cell_5(con, player)
            time.sleep(0.2)
            destroy_lw_cell_5(con, player)
            tcod.console_flush()
            clear_all()

            render_map()
            render_all_entities()
            build_lw_cell_6(con, player)
            time.sleep(0.2)
            destroy_lw_cell_6(con, player)
            tcod.console_flush()
            clear_all()

            render_map()
            render_all_entities()
            build_lw_cell_7(con, player)
            time.sleep(0.2)
            destroy_lw_cell_7(con, player)
            tcod.console_flush()
            clear_all()

            render_map()
            render_all_entities()
            build_lw_cell_7(con, player)
            time.sleep(0.2)
            destroy_lw_cell_7(con, player)
            tcod.console_flush()
            clear_all()

            render_map()
            render_all_entities()
            build_lw_cell_6(con, player)
            time.sleep(0.2)
            destroy_lw_cell_6(con, player)
            tcod.console_flush()
            clear_all()

            render_map()
            render_all_entities()
            build_lw_cell_5(con, player)
            time.sleep(0.2)
            destroy_lw_cell_5(con, player)
            tcod.console_flush()
            clear_all()

            render_map()
            render_all_entities()
            build_lw_cell_4(con, player)
            time.sleep(0.2)
            destroy_lw_cell_4(con, player)
            tcod.console_flush()
            clear_all()

            render_map()
            render_all_entities()
            build_lw_cell_3(con, player)
            time.sleep(0.2)
            destroy_lw_cell_3(con, player)
            tcod.console_flush()
            clear_all()

            render_map()
            render_all_entities()
            build_lw_cell_2(con, player)
            time.sleep(0.2)
            destroy_lw_cell_2(con, player)
            tcod.console_flush()
            clear_all()

            render_map()
            render_all_entities()
            build_light_walker(con, player)
            destroy_light_walker(con, player)
            tcod.console_flush()
            clear_all()
            build = False
        else:
            render_map()
            render_all_entities()
            build_light_walker(con, player)
            destroy_light_walker(con, player)
            tcod.console_flush()
            clear_all()



        

        # We hand over the current key result into the handle_keys function
        # This function returns a library for us that we name action
        action = handle_keys(keyboard_activity)

        # We check this library for various results using the get method
        move = action.get('move')
        exit = action.get('exit')
        # exit_walker = action.get('exit_walker')
        # enter_walker = action.get('enter_walker')

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
            solo = False

        # Another boolean value which triggers a method setting fullscreen.  tcod.console_is_fullscreen() currently returns False
        # By adding not before it we change the value to True which changes the game to fullscreen.
        if fullscreen:
            solo = True




if __name__ == '__main__':
    main()