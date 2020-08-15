#! python3

import pyautogui
from inputs import get_gamepad
import keyboard
import multiprocessing
import re
import json

pyautogui.PAUSE = 0

welcome = '''
Welcome to NeoGeo training mode
Press select to take/stop control of P2
Press coin to start recording
Press a to stop recording
Press start to play recorded inputs
Quit NeoGeo training mode witch ctrl-pause
'''

# Lecture fichier de conf
with open('garou.ini') as file:
    conf_content = file.readlines()
# déclaration du fichier de conf de sortie
conf_output = {}

# parsing du fichier de conf pour retirer le scancode et le nom de l'input
for line in conf_content:
    match = re.search("^input", line)
    if match:
        line_table = re.split(r"\s{2,}", line)
        conf_output.update({line_table[1].replace("\"", ""): line_table[2].replace("\n", "").replace("switch ",
                                                                                                     "").replace(
            "constant ", "")})

json_db = '''{
   "0x4005":"ABS_Z",
   "0x4084":"BTN_TL",
   "0x4087":"BTN_SELECT",
   "0x4086":"BTN_START",
   "0x4013":"ABS_HAT0Y",
   "0x4012":"ABS_HAT0Y",
   "0x4010":"ABS_HAT0X",
   "0x4011":"ABS_HAT0X",
   "0x4082":"BTN_WEST",
   "0x4080":"BTN_SOUTH",
   "0x4083":"BTN_NORTH",
   "0x4081":"BTN_EAST",
   "0x4085":"BTN_TR",
   "0x4004":"ABS_RZ",
   "0x01":"ESCAPE",
   "0x02":"1",
   "0x03":"2",
   "0x04":"3",
   "0x05":"4",
   "0x06":"5",
   "0x07":"6",
   "0x08":"7",
   "0x09":"8",
   "0x0A":"9",
   "0x0B":"0",
   "0x0C":"MINUS",
   "0x0D":"EQUALS",
   "0x0E":"BACK",
   "0x0F":"TAB",
   "0x10":"q",
   "0x11":"z",
   "0x12":"e",
   "0x13":"r",
   "0x14":"t",
   "0x15":"y",
   "0x16":"u",
   "0x17":"i",
   "0x18":"o",
   "0x19":"p",
   "0x1A":"LBRACKET",
   "0x1B":"RBRACKET",
   "0x1C":"RETURN",
   "0x1D":"LCONTROL",
   "0x1E":"a",
   "0x1F":"s",
   "0x20":"d",
   "0x21":"f",
   "0x22":"g",
   "0x23":"h",
   "0x24":"j",
   "0x25":"k",
   "0x26":"l",
   "0x27":"SEMICOLON",
   "0x28":"APOSTROPHE",
   "0x29":"GRAVE",
   "0x2A":"LSHIFT",
   "0x2B":"BACKSLASH",
   "0x2C":"z",
   "0x2D":"x",
   "0x2E":"c",
   "0x2F":"v",
   "0x30":"b",
   "0x31":"n",
   "0x32":"m",
   "0x33":"COMMA",
   "0x34":"PERIOD",
   "0x35":"SLASH",
   "0x36":"RSHIFT",
   "0x37":"MULTIPLY",
   "0x38":"LMENU",
   "0x39":"SPACE",
   "0x3A":"CAPITAL",
   "0x45":"NUMLOCK",
   "0x46":"SCROLL",
   "0x47":"NUMPAD7",
   "0x48":"NUMPAD8",
   "0x49":"NUMPAD9",
   "0x4A":"SUBTRACT",
   "0x4B":"NUMPAD4",
   "0x4C":"NUMPAD5",
   "0x4D":"NUMPAD6",
   "0x4E":"ADD",
   "0x4F":"NUMPAD1",
   "0x50":"NUMPAD2",
   "0x51":"NUMPAD3",
   "0x52":"NUMPAD0",
   "0x53":"DECIMAL",
   "0x56":"OEM_102",
   "0x70":"KANA",
   "0x73":"ABNT_C1",
   "0x79":"CONVERT",
   "0x7B":"NOCONVERT",
   "0x7D":"YEN",
   "0x7E":"ABNT_C2",
   "0x8D":"NUMPADEQUALS",
   "0x90":"PREVTRACK",
   "0x91":"AT",
   "0x92":"COLON",
   "0x93":"UNDERLINE",
   "0x94":"KANJI",
   "0x95":"STOP",
   "0x96":"AX",
   "0x97":"UNLABELED",
   "0x99":"NEXTTRACK",
   "0x9C":"NUMPADENTER",
   "0x9D":"RCONTROL",
   "0xA0":"MUTE",
   "0xA1":"CALCULATOR",
   "0xA2":"PLAYPAUSE",
   "0xA4":"MEDIASTOP",
   "0xAE":"VOLUMEDOWN",
   "0xB0":"VOLUMEUP",
   "0xB2":"WEBHOME",
   "0xB3":"NUMPADCOMMA",
   "0xB5":"DIVIDE",
   "0xB7":"SYSRQ",
   "0xB8":"RMENU",
   "0xC5":"PAUSE",
   "0xC7":"HOME",
   "0xC8":"UP",
   "0xC9":"PRIOR",
   "0xCB":"LEFT",
   "0xCD":"RIGHT",
   "0xCF":"END",
   "0xD0":"DOWN",
   "0xD1":"NEXT",
   "0xD2":"INSERT",
   "0xD3":"DELETE",
   "0xDB":"LWIN",
   "0xDC":"RWIN",
   "0xDD":"APPS",
   "0xDE":"POWER",
   "0xDF":"SLEEP",
   "0xE3":"WAKE",
   "0xE5":"WEBSEARCH",
   "0xE6":"WEBFAVORITES",
   "0xE7":"WEBREFRESH",
   "0xE8":"WEBSTOP",
   "0xE9":"WEBFORWARD",
   "0xEA":"WEBBACK",
   "0xEB":"MYCOMPUTER",
   "0xEC":"MAIL",
   "0xED":"MEDIASELECT"
}'''

data = json.loads(json_db)


# Variables

def mappingValue(dictDb, valueToFind):
    for key, value in dictDb.items():
        if key == conf_output[valueToFind]:
            return value


p1Up = mappingValue(data, 'P1 Up')
p1Down = mappingValue(data, "P1 Down")
p1Left = mappingValue(data, "P1 Left")
p1Right = mappingValue(data, "P1 Right")
p1A = mappingValue(data, "P1 Button A")
p1B = mappingValue(data, "P1 Button B")
p1C = mappingValue(data, "P1 Button C")
p1D = mappingValue(data, "P1 Button D")
p1Dummy = mappingValue(data, "P1 Select")
p1Record = mappingValue(data, "P1 Coin")
p1Play = mappingValue(data, "P1 Start")
p2Up = mappingValue(data, "P2 Up")
p2Down = mappingValue(data, "P2 Down")
p2Left = mappingValue(data, "P2 Left")
p2Right = mappingValue(data, "P2 Right")
p2A = mappingValue(data, "P2 Button A")
p2B = mappingValue(data, "P2 Button B")
p2C = mappingValue(data, "P2 Button C")
p2D = mappingValue(data, "P2 Button D")
stop = "a"
print("end mapping")


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
    global recorded
    while True:
        for event in get_gamepad():
            try:
                if event.code == p1Record and event.state > int(0):
                    print('Record P2')
                    print("Press the", stop, "button to quit record")
                    recorded = keyboard.record(until=stop)
                    print('End record')
                elif event.code == p1Play and event.state > int(0):
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
