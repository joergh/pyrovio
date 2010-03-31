To use:

import rovio
import time

r = rovio.Rovio( '192.168.0.10' ) # ip addess of rovio

# start at the rover's home
r.api.go_home()
r.forward()
r.forward_left(speed=4)
r.right()
r.backward()
r.rotate_right(speed=9,angle=90)
time.sleep(3) # let operation finish
r.turn_around(speed=2)
time.sleep(3)
r.back_right(speed=4)

r.head_up()
time.sleep(2)
r.head_middle()
time.sleep(2)
r.head_down()
time.sleep(2)

# run back and forth
for x in range(4):
    r.patrol(speed=5) 

print r.battery()
#go back and recharge
r.api.go_home_and_dock()
# your battery only lasts a couple of minutes try:
# this may fix it.
r.dock_and_undock()
