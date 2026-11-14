from pyautogui import click
import random
from time import sleep
random.seed(a=None, version=2)
freq = input('set click frequency: ')
ymax = input('set monitor pixel length(the bigger number, e.g. 1920): ')
xmax = input('set monitor pixel height(the smaller number, e.g. 1080): ')

while True:
    delay = random.randint(1, int(freq))
    sleep(delay)
    click(random.randint(1, int(xmax)-1), random.randint(1, int(ymax)-1))