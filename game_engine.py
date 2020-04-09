import tcod
from game.variables import *
from game.input import handle_keys

def main():

    me_x = int(screen_width / 2)
    me_y = int(screen_height / 2)

    tcod.console_set_custom_font('arial10x10.png', tcod.FONT_TYPE_GRAYSCALE | tcod.FONT_LAYOUT_TCOD)

    tcod.console_init_root(screen_width, screen_height, 'Platform 50', False)
    con = tcod.console_new(screen_width, screen_height)

    key = tcod.Key()
    mouse = tcod.Mouse()

    while not tcod.console_is_window_closed():
        tcod.sys_check_for_event(tcod.EVENT_KEY_PRESS, key, mouse)

        tcod.console_set_default_foreground(con, tcod.orange)
        tcod.console_put_char(con, me_x, me_y, '@', tcod.BKGND_NONE)
        tcod.console_put_char(con, me_x - 1, me_y, '[', tcod.BKGND_NONE)
        tcod.console_put_char(con, me_x + 1, me_y, ']', tcod.BKGND_NONE)
        tcod.console_put_char(con, me_x - 2, me_y, '[', tcod.BKGND_NONE)
        tcod.console_put_char(con, me_x + 2, me_y, ']', tcod.BKGND_NONE)
        tcod.console_put_char(con, me_x - 3, me_y, ':', tcod.BKGND_NONE)
        tcod.console_put_char(con, me_x + 3, me_y, ':', tcod.BKGND_NONE)
        tcod.console_put_char(con, me_x - 1, me_y + 1, '|', tcod.BKGND_NONE)
        tcod.console_put_char(con, me_x + 1, me_y + 1, '|', tcod.BKGND_NONE)


        #  Console_blit is bringing forth our new console as the default viewable console.
        tcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)
        
        tcod.console_flush()

        tcod.console_put_char(con, me_x, me_y, ' ', tcod.BKGND_NONE)
        tcod.console_put_char(con, me_x - 1, me_y, ' ', tcod.BKGND_NONE)
        tcod.console_put_char(con, me_x + 1, me_y, ' ', tcod.BKGND_NONE)
        tcod.console_put_char(con, me_x - 2, me_y + 1, ' ', tcod.BKGND_NONE)
        tcod.console_put_char(con, me_x + 2, me_y + 1, ' ', tcod.BKGND_NONE)
        tcod.console_put_char(con, me_x - 3, me_y, ' ', tcod.BKGND_NONE)
        tcod.console_put_char(con, me_x + 3, me_y, ' ', tcod.BKGND_NONE)
        tcod.console_put_char(con, me_x - 1, me_y + 1, ' ', tcod.BKGND_NONE)
        tcod.console_put_char(con, me_x + 1, me_y + 1, ' ', tcod.BKGND_NONE)

        # We hand over the current key result into the handle_keys function
        # This function returns a library for us that we name action
        action = handle_keys(key)

        # We check this library for various results using the get method
        move = action.get('move')
        exit = action.get('exit')
        fullscreen = action.get('fullscreen')


        if move:
            dx, dy = move # When we used get on 'move' the result is a list of two numbers (if move even happened)
            me_x += dx
            me_y += dy # Depending on which key we pressed the values are calculated and updated so we move in the correct direction

        # This dictionary key returns a boolean value that then says to return True which breaks the game loop.
        if exit:
            return True

        # Another boolean value which triggers a method setting fullscreen.  tcod.console_is_fullscreen() currently returns False
        # By adding not before it we change the value to True which changes the game to fullscreen.
        if fullscreen:
            tcod.console_set_fullscreen(not tcod.console_is_fullscreen())




if __name__ == '__main__':
    main()