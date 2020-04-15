# Platform 50
A Roguelike game focused around Mechs known as Walkers.  You have to leave your Walker in order to pickup/install anything.  And you can either move up or move down using service elevators.  The direction you choose effects the rules of the game.  Platform 50 has two doors on each side of the room.  The doors lead to identical rooms.  Platform 50 will most likely be the only static map in the game where as we move up or down we will find procedurally generated levels.

This will be created using Python and tcod mostly.  I'm only in the 'proof of concept' stage for most of this but I do plan on pushing code through very soon.

E.T. Deubner - April 9, 2020

Well.  Everything worked exactly like I hoped it would and I'm able to render and take control of a Mech-like thing that I'm calling Walkers using only ASCII.  I'm getting ready to put all the 'walkers' code into its own module and then very soon I'll start working on being able to enter and exit the Walker on the fly.  I need to take a step back from the code and actually put down some real 'strategies' instead of just winging it as I go forward.  To be honest I thought it would take longer to even get this working so yea... pretty cool stuff.  I think might actually work.  And be fun too!!!!

E.T. Deubner - April 9, 2020 - 4:00PM

I'm on the final stretch to get a basic working version of stepping up to Walker and then activating it to get in.  The Walker will spring to life and allow your '@' to jump on board and start pioliting it.  I've done all the proof of concepts so I know everything is possible.  Just need to do the work now.  Hopefully by tomorrow I'll have something to show and I can post a little demo on Reddit and let people check it out themselves if they wanna play around with it.

E.T. Deubner - April 10, 2020

Updated a requirements.txt so as of right now, anything thats on GitHub can be cloned then you should set up a virtual environment (Python 3.7.3), install the requirements.txt using pip and run the program with 'python game_engine.py'.  Unfortuantely there isn't anything impressive there yet.  Just wanted to get that set up because I was probably going to forget.

E.T.D. - April 10 - 8pm

You can now "get in" the Walker and walk around then "get out" and walk around separately.  When you first start, you'll be sitting in the Walker but not piloting it yet.  If you move around you'll be separate.  Stay in the original position or go back to the original position and hit ESC.  Wait a few seconds.  Then the animation will kick in.  Once it looks like it did when you hit ESC, now you'll be able to move the whole thing around.  If you hit ENTER you will "exit" the vehicle.  

Unfortunately the Walkers coordinates are tied to one spot at the moment so if you exit the Walker somewhere else it will apear where it started from.  If you walk back up to it and hit ESC you'll take it over again but the animation won't play again.
I'll need to copy the current coordinates before saving a new Entity so you can get out anywhere.

I also need to simplify the build/destroy functions down to one function that takes coordinates.  As well as clean things up in the game_engine.py and inputs.py.  The good news is the proof of concept was successful.  I just have tidy things up now and hopefully move forward.  The next thing I'd like to do is start working on how the inventory system will work when separating from the walker.  

E.T.D. - April 15
