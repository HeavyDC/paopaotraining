#! python3

import pyautogui
from inputs import get_gamepad
import keyboard
import time
import multiprocessing
import configparser as cp
pyautogui.PAUSE = 0

welcome = '''
Welcome to NeoGeo training mode
Press dummy_control to take/stop control of P2
Press dummy_record to record input
Press dummy_play to play recorded inputs
Quit NeoGeo training mode witch ctrl-pause
'''

# Lecture fichier de conf
config = cp.ConfigParser()
config.read('input_map.ini')

# Variables p-1
p1Up = config.get('p1 controls', 'P1-up')
p1Down = config.get('p1 controls', 'P1-down')
p1Left = config.get('p1 controls', 'P1-left')
p1Right = config.get('p1 controls', 'P1-right')
p1A = config.get('p1 controls', 'P1-A')
p1B = config.get('p1 controls', 'P1-B')
p1C = config.get('p1 controls', 'P1-C')
p1D = config.get('p1 controls', 'P1-D')
p1Dummy = config.get('p1 controls', 'P1-dummy')

# Variables p-2

p2Up = config.get('p2 controls', 'P2-up')
p2Down = config.get('p2 controls', 'P2-down')
p2Left = config.get('p2 controls', 'P2-left')
p2Right = config.get('p2 controls', 'P2-right')
p2A = config.get('p2 controls', 'P2-A')
p2B = config.get('p2 controls', 'P2-B')
p2C = config.get('p2 controls', 'P2-C')
p2D = config.get('p2 controls', 'P2-D')

# Variables record
record = config.get('record controls', 'record')
stop = config.get('record controls', 'stop')
play = config.get('record controls', 'play')


def p1_to_p2():
    while True:
        events = get_gamepad()
        for event in events:
            # direction vers le bas
            if event.code == p1Down:
                if event.state == 1:
                    print('Crouch!')
                    pyautogui.keyDown(p2Down)
                elif event.state == 0:
                    pyautogui.keyUp(p2Down)
            # direction vers le haut
            if event.code == p1Up:
                if event.state == -1:
                    print('Jump!')
                    pyautogui.keyDown(p2Up)
                elif event.state == 0:
                    pyautogui.keyUp(p2Up)
            # direction vers la gauche
            if event.code == p1Left:
                if event.state == -1:
                    print('Left!')
                    pyautogui.keyDown(p2Left)
                elif event.state == 0:
                    pyautogui.keyUp(p2Left)
            # direction vers la droite
            if event.code == p1Right:
                if event.state == 1:
                    print('Right!')
                    pyautogui.keyDown(p2Right)
                elif event.state == 0:
                    pyautogui.keyUp(p2Right)
            # bouton A
            if event.code == p1A:
                if event.state > 0:
                    print('A!')
                    pyautogui.keyDown(p2A)
                elif event.state == 0:
                    pyautogui.keyUp(p2A)
            # bouton B
            if event.code == p1B:
                if event.state > 0:
                    print('B!')
                    pyautogui.keyDown(p2B)
                elif event.state == 0:
                    pyautogui.keyUp(p2B)
            # bouton C
            if event.code == p1C:
                if event.state > 0:
                    print('C!')
                    pyautogui.keyDown(p2C)
                elif event.state == 0:
                    pyautogui.keyUp(p2C)
            # bouton D
            if event.code == p1D:
                if event.state > 0:
                    print('D!')
                    pyautogui.keyDown(p2D)
                elif event.state == 0:
                    pyautogui.keyUp(p2D)
        # stop p1 vers p2
        if event.code == p1Dummy and event.state > int(0):
            print('P2 STOP')
            # reset positions
            pyautogui.keyUp(p2Up)
            pyautogui.keyUp(p2Left)
            pyautogui.keyUp(p2Down)
            pyautogui.keyUp(p2Right)
            break
    while True:
        for event in get_gamepad():
            if event.code == p1Dummy and event.state > int(0):
                print('P2 START')
                p1_to_p2()

def dummy_record():
    while True:
        for event in get_gamepad():
            try:
                if event.code == record and event.state > int(0):
                    print('Record P2')
                    print("Press the",stop, "button to quit record")
                    recorded = keyboard.record(until=stop)
                    print('End record')
                elif event.code == play and event.state > int(0):
                    print('Start replay')
                    keyboard.play(recorded)
                    print('End replay')
            except:
                print("Nothing recorded")
                pass

if __name__ == '__main__':
    print(welcome)
    while True:
        for event in get_gamepad():
            if event.code == p1Dummy and event.state > int(0):
                print('P2 START')
                # p1_to_p2()
                # dummy_record()
                p = multiprocessing.Process(target=p1_to_p2)
                q = multiprocessing.Process(target=dummy_record)
                p.start()
                q.start()
                p.join()
                q.join()