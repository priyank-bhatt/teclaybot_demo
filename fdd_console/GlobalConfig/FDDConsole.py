#!/usr/bin/python

import pyautogui
import time
from configparser import ConfigParser

configur = ConfigParser()
configur.read('fdd_console\GlobalConfig\config.ini')
FDD_application = configur.get('Application', 'fdd_console')
Stream_folder = configur.get('Streams', 'framerate_streams')

load_button = configur.get('FDD_Buttons', 'load_button')
start_button = configur.get('FDD_Buttons', 'start_button')
framerate_button = configur.get('FDD_Buttons', 'framerate_button')
mode_button = configur.get('FDD_Buttons', 'playback_mode_button')

time.sleep(4)

# Open start menu, search for FDD console and open it
pyautogui.hotkey("win", "r")
time.sleep(2)
pyautogui.typewrite(FDD_application)
time.sleep(2)
pyautogui.hotkey("enter")

# Maximize the FDD console, load stream and set the configuration
time.sleep(60)
pyautogui.hotkey("win", "up")
time.sleep(2)

# Locate load button, click it and add stream folder
b = pyautogui.locateCenterOnScreen(load_button)
time.sleep(1)
pyautogui.click(b[0], b[1])
time.sleep(2)
pyautogui.typewrite(Stream_folder)
pyautogui.hotkey("enter")
time.sleep(1)
pyautogui.hotkey("enter")
time.sleep(2)

# Locate framerate tab and set to 23.976 and locate playback mode tab adn set to file-based
f = pyautogui.locateCenterOnScreen(framerate_button)
time.sleep(1)
pyautogui.click(f[0], f[1]+25)
time.sleep(2)
pyautogui.click(f[0], f[1]+48)
time.sleep(2)

m = pyautogui.locateCenterOnScreen(mode_button)
time.sleep(1)
pyautogui.click(m[0], m[1]+25)
time.sleep(2)
pyautogui.click(m[0], m[1]+48)
time.sleep(2)

# Locate the start ananlysis button and click to start analysis
b = pyautogui.locateCenterOnScreen(start_button)
time.sleep(1)
pyautogui.click(b[0], b[1])
time.sleep(10)
pyautogui.hotkey('enter')
time.sleep(150)

# Click enter for pop-up window
pyautogui.hotkey('enter')
time.sleep(2)

# Close the FDD console application
pyautogui.hotkey('altleft', 'fn', 'f4')
