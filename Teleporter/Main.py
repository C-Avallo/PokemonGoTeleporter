import File_Reader
import Notifaction
import webbrowser
import time
import os
import time
import string
from types import *
import Command_Line_Functions
import Loading_Bar
import sys







import Prompts
get_prompt = Prompts.Prompting()
move_speed = get_prompt.get_speed()

Command_Line_Functions.confirmMirror()
Command_Line_Functions.confirmXcode()

import Map_Plotter

displaycoords = Map_Plotter.Display()
bot = File_Reader.Teleport()
notify = Notifaction.DoNotifaction()
displaycoords.openChooseLocation()
Command_Line_Functions.chromeFront()

ChoosenLocation = False
while not ChoosenLocation:
    try:
        displaycoords.getLat_Test()
        break
    except:
        ChoosenLocation = False
    time.sleep(.01)

ChoosenLocation = True
time.sleep(1)

SpawnX = displaycoords.getLat(); SpawnY = displaycoords.getLong()

Lati = SpawnX; Longi = SpawnY

bot.TeleportTo(Lati, Longi)


os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (1100,200)
import pygame
pygame.init()
pygame.font.init()


SCREEN_SIZE = (200, 450)
display = pygame.display.set_mode(SCREEN_SIZE)
myfont = pygame.font.SysFont('Comic Sans MS', 20); infofont = pygame.font.SysFont('Comic Sans MS', 15)
pygame.display.set_caption("Character Controller", "Character Controller")
clock = pygame.time.Clock()
pokeball = pygame.image.load('Pokeball_200.png')

Command_Line_Functions.show_loading_info()

from selenium import webdriver

#browser = webdriver.Chrome()
#browser.set_window_position(700, 0)
#browser.set_window_size(600, 1000)
#browser.get('https://thesilphroad.com/atlas#4.55/{}/{}"'.format(str(Lati), str(Longi)))


displaycoords.DisplayCoords(str(Lati),str(Longi))


while True:


    display.fill((255, 255, 255)) #white

    Controls = infofont.render('Arrow Keys (Move) - W&S (Speed) - K(Kill)', False, (0, 0, 0))
    Latitude_Text = myfont.render('Latitude: ' + str(Lati), False, (0,0,0))
    Longitude_Text = myfont.render('Longitude: ' + str(Longi), False, (0,0,0))
    Python_Version = myfont.render('Running Python: ' + str(sys.version.split(' ')[0]), False, (0,0,0))

    display.blit(Controls, (0, 1))
    display.blit(Latitude_Text, (20, 50))
    display.blit(Longitude_Text, (20, 100))
    display.blit(Python_Version, (20, 150))
    display.blit(pokeball, (0, 200))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            notify.notify("Quitting App", "")
            pygame.quit(); 

        if event.type == pygame.KEYDOWN:
            Command_Line_Functions.update()

            if event.key == pygame.K_LEFT:
                print("Moving Left")
                Longi -= move_speed
                bot.TeleportTo(format(Lati, '.6f'), format(Longi, '.6f'))


            if event.key == pygame.K_RIGHT:
                print("Moving Right")
                Longi += move_speed
                bot.TeleportTo(format(Lati, '.6f'), format(Longi, '.6f'))


            if event.key == pygame.K_UP:
                print("Moving Forward")
                Lati += move_speed
                bot.TeleportTo(format(Lati, '.6f'), format(Longi, '.6f'))


            if event.key == pygame.K_DOWN:
                print("Moving Down")
                Lati -= move_speed
                bot.TeleportTo(format(Lati, '.6f'), format(Longi, '.6f'))


            if event.key == pygame.K_w:
                Command_Line_Functions.say("Speed Increase")
                move_speed += 0.0001
                notify.notify("Speed Increased by: " + "+0.0001 |" + " Speed: " + str(move_speed), "Easy Walk")


            if event.key == pygame.K_s:
                Command_Line_Functions.say("Speed Decrease")
                move_speed -= 0.0001
                notify.notify("Speed Decreased by: " + "-0.0001 |" + " Speed: " + str(move_speed), "Easy Walk")

            if event.key == pygame.K_k:
                notify.notify("Quitting Processes", "Easy Walk")
                os.system("pkill -f 'osascript'")


            if event.key == pygame.K_t:

                from pymsgbox import *
                from pygame.locals import *
                lat_extract = prompt(text='Enter Latitude to Teleport to', title='Info')
                long_extract = prompt(text='Enter Longitude to Teleport to', title='Info')
                Longi = format(float(long_extract), '.6f')
                Lati = format(float(lat_extract), '.6f')
                bot.TeleportTo(format(Lati, '.6f'), format(Longi, '.6f'))



    clock.tick(3)


