import os
import pyautogui
import time
from PIL import Image, ImageGrab
import numpy as np
import pyperclip
import a_etoile


SCREEN_W = 750
SCREEN_H = 500
BARRE = 40
SPEED = 0.2

def takeSC():
    print("6")
    i = 0
    pyperclip.copy('')

    pyautogui.hotkey('alt', 'prtsc')

    while(ImageGrab.grabclipboard() == None):
        print("1")

    image = ImageGrab.grabclipboard()

    try:
        data = np.asarray(image, dtype=np.int32)
    except:
        print("except")
        image = ImageGrab.grabclipboard()

    data = np.delete(data, SCREEN_W+1, 1)
    data = np.delete(data, 0, 1)
    data = np.delete(data, SCREEN_H+BARRE-1, 0)

    for ligne in range(BARRE-1):
        data = np.delete(data, ligne-ligne, 0)

    return data

def pos(data):
    print("3")
    serpent, food = None, None
    for y in range(40):
        for x in range(60):
            if(data[int(y*(SCREEN_H/40))+5][int(x*(SCREEN_W/60))+5][0] == 50):
                serpent = (y, x)
            if(data[int(y*(SCREEN_H/40))+5][int(x*(SCREEN_W/60))+5][0] == 213):
                food = (y, x)
            if(serpent != None and food != None):
                return serpent, food

pyautogui.FAILSAFE = True

for i in range(3):
    print(".")
    time.sleep(1)

while 1:
    print("2")
    data = takeSC()

    if(data[5][5][0] == 250):
        print("5")
        pyautogui.hotkey('r')
    else:
        serpent, food = pos(data)

        dy = food[0] - serpent[0]
        dx = food[1] - serpent[1]

        path = a_etoile.astar(data, serpent, food)
        path = a_etoile.posToMove(path)

        for move in path:
            pyautogui.hotkey(move)
            time.sleep(SPEED)
