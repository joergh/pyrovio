import pygame
import rovio
import time

Host="192.168.1.19"
User=None
Password=None
Port=80

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

while(True):
    evt = pygame.event.wait()
    if evt.type==pygame.QUIT:
        break

rov.stop_stream_handler()
pygame.quit()
