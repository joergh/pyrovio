""" 
A very simple demonstration program to show the stream handler functionality.
This can be used to continuously acquire jpeg images fom the rovio while doing
other things.

To end this program, simply close the window.

Needs pyGame to run
"""

import pygame
import rovio
import time

Host="192.168.1.19"
User=None
Password=None
Port=80

accepted_keys = (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)
                 
def image_handler(img):
    image=pygame.image.load(img,"cam.jpg")
    display.blit(image, (0,0))
    pygame.display.update()
   
def status_handler(status):
    print status
    
pygame.init()
pygame.display.init()

display = pygame.display.set_mode((640,480))

rov = rovio.Rovio(Host, User, Password, Port)
rov.api.change_framerate(5)
rov.api.change_resolution(3)

rov.setup_stream_handler(True, image_handler, None)

drive_speed = 5
rot_speed = 6

button = None
run = True
while(run):
    events = pygame.event.get()
    for evt in events:
        if evt != None:
            if evt.type == pygame.QUIT:
                run = False
            elif evt.type == pygame.KEYDOWN:
                if evt.key in accepted_keys:
                    button = evt.key
            elif evt.type == pygame.KEYUP:
                button = None
              
    if button != None:
        if button == pygame.K_UP:
            rov.forward(drive_speed)
        elif button == pygame.K_DOWN:
            rov.backward(drive_speed)
        elif button == pygame.K_RIGHT:
            rov.rotate_right(rot_speed)
        elif button == pygame.K_LEFT:
            rov.rotate_left(rot_speed)
    
    time.sleep(0.1)
    
rov.stop_stream_handler()
pygame.quit()
