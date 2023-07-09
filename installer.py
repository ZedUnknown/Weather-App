import os
import sys
import time

def installing():
    os.system('cls' if os.name == 'nt' else 'clear')
    SlowType('Installing', 0.04)

def SlowType(text: str, speed: float, newLine=True):
    for i in text:
        print(i, end="", flush=True)
        time.sleep(speed)
    if newLine:
        print()

def modules():
    try:
        os.system("cls" if os.name == 'nt' else "clear")
        version = sys.version
        major = version[0]
        minor = version[2:4]
        micro = version[5]

        if int(major) >= 3:
            modules_to_install = []
            try:
                with open('requirements.txt', 'r') as file:
                    modules_to_install = [line.strip() for line in file if '\n']
                    num_modules = len(modules_to_install)
                    SlowType(f"Installing {num_modules} modules...", 0.02)
                    for module in modules_to_install:
                        SlowType(f"\n[===[{module}]===]", 0.02)
                        os.system(f'py -m pip install {module}')
            
            except Exception as e:
                input(f'Error has occured: {e}\n Press ENTER to exit!')
                 
                
        else:
            print("--> ")
            SlowType(f"Your python version is {major}.{minor}.{micro}\n performing upgrade to a new version!")
            os.system('py -m pip install --upgrade pip')
            modules()

    except ConnectionError or ConnectionAbortedError or ConnectionRefusedError:
        input("Connection Error!\nPress ENTER to exit")
        exit()



modules()
