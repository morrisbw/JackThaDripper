# JackThaDripper
JackThaDripper2.py is my first experiment with  tkinter.
It's primary function is to produce G-code for filling molds with a custom designed syringe mechanism mounted to a 3d printer.

There's no defensive programming for inputs. Just experimenting.

Volume is not yet mapped to any actual volume, just the values that are sent to the extruder.
You can do a 1x1 grid test to determine the actual value to send the extruder.
*The first change in direction of the syringe needs a slight adjustment so the first hole gets a precise amount.

It must be run with the syringe all the way down, ready to be filled. There is no end stop for the extruder on 3d printers, so we cannot detect it's position with this program. Pronterface is necessary to manually "home" the syringe when necessary. 

The other axis are challenging as well because of the physical design of this mechanism, but can be done programmatically. The device is designed to extract from a reservoir below the print bed. Step one is to move the bed out of the way by homing the Y axis.

Next we need to make sure the syringe is not so low that it will hit the base rails at the bottom of the printer. So I move the Z axis up high enough so that if it was at the bottom, it would now be above the base rail of the machine.
Now I can home the x axis. and move the x axis over to a known 40mm, directly above the reservoir.
Homing z puts the syringe at the bottom of the reservoir.

Through some tinkering in pronterface, I determined the max capacity of my syringe(in terms of gcode). It would be a small step further to map to an actual volume. 
