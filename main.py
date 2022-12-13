import pyautogui
from time import sleep
from datetime import datetime
import os
import keyboard


def screenshot(fp='./screenshot.png'):
    im = pyautogui.screenshot()

    path = os.path.dirname(fp)
    if not os.path.exists(path):
        os.makedirs(path)
    
    im.save(fp)


def click(pos):
    x, y = pos['position']
    x, y = int(x), int(y)

    pyautogui.moveTo(x, y)
    pyautogui.click()


def is_pixel_color(pos):
    x, y = pos['position']
    x, y = int(x), int(y)
    color = pos['color']

    pixel = pyautogui.pixel(x, y)
    c = [abs(x[0]-x[1]) < 10 for x in zip(color, pixel)]

    return all(c)


size = pyautogui.size()

# Positions calculated with the size of the window and the relative
# position of the pixel to work with any resolution
items = {
    "loot_inv": {
        'position': (int(int(size[0] * 0.046875)), int(size[1] * 0.28241)),
        'color': [255, 255, 255]
    },
    "open_button": {
        'position': (int(size[0] * 0.1), int(size[1] * 0.862)),
        'color': [41, 107, 158]
    },
    "yes_button": {
        'position': (int(size[0] * 0.44), int(size[1] * 0.571)),
        'color': [255, 255, 255] # Doesn't matter
    },
    "ok_button": {
        'position': (int(size[0] * 0.564), int(size[1] * 0.924)),
        'color': [160, 246, 255]
    },
    "ok_button2": {
        'position': (int(size[0] * 0.5), int(size[1] * 0.912)),
        'color': [255, 255, 255]
    },
    "back_button": {
        'position': (int(size[0] * 0.067), int(size[1] * 0.95)),
        'color': [255, 255, 255]
    },
}

pos = (int(size[0] * 0.635), int(size[1] * 0.208))
rarities = {
    "uncommon": { 
        'position': pos,
        'color': [81, 128, 147]
    },
    "rare": { 
        'position': pos,
        'color': [73, 93, 146]
    },
    "very_rare": {
        'position': pos,
        'color': [93, 75, 148]
    },
    "import": {
        'position': pos,
        'color': [145, 44, 46]
    },
}

print('== ROCKET LEAGUE LOOT OPENER ==')
print('Make sure that the loot box is in the first slot. (You can filter the inventory)')
print('Press enter to start...')
input()
print('Starting... (Keep C pressed to stop)')

click({'position': (1,1)}) #To click out of the terminal
while is_pixel_color(items['loot_inv']):
    if keyboard.is_pressed('c'):
        print('Stopped')
        break

    click(items['loot_inv'])
    sleep(1)

    while is_pixel_color(items['open_button']):
        if keyboard.is_pressed('c'):
            print('Stopped')
            break

        print('Opening loot')
        click(items['open_button'])
        sleep(0.5)
        click(items['yes_button'])
        
        c = 0
        rarity = 'unknown'
        while True:
            for rarity_ in rarities:
                if is_pixel_color(rarities[rarity_]):
                    rarity = rarity_
                    break
            
            sleep(1)
            c += 1
            if ((c > 20) or (rarity != 'unknown')):
                break

        print(f'Found {rarity} item')
        fp = os.path.join('loots', rarity, f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.png')
        screenshot(fp)

        if is_pixel_color(items['ok_button']):
            click(items['ok_button'])
        else:
            click(items['ok_button2'])

        sleep(2)

    click(items['back_button'])
    sleep(10)
   