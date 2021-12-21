from defaults import *
from gameClasses import *
from player import *
import threading
import os

player = Player("lucas", returnDefaultServers(), None)

testing = True

def main():
    global player
    print("HackingSystem v1.3")
    while True:
        if player.curSystemPort == None:
            action = input(f"[{player.curSystemIp}/home~]>")
        else:
            action = input(f"[{player.curSystemIp}/{player.curSystemPort}~]>")
        
        if action.startswith("scan") and "-s" in action:
            for x in player.formatGetServers():
                print('-'*20)
                print(f'Name:{x["name"]}\nIP:{x["ip"]}\nHackLvl:{x["hackLvl"]}\nRoot access:{x["root"]}')
                print()
        if action.startswith("get -root"):
            serverip = action.split()[2]
            response = player.gainServerRoot(serverip)
            if response:
                print(f"Gained root on ({serverip}) and entered the server")
            else:
                print(f'Failed for a reason :(')
        
        if action.startswith("connect -s"):
            serverip = action.split()[2]
            response = player.enterServer(serverip)
            if response:
                print(f"Connected to ({serverip})")

        elif action.startswith("connect") and "-h" in action:
            player.exitServers()
            print("Returned to local machine")

        if action == "clear" or action == "cls" or "-C" in action:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("HackingSystem v1.3")
def test():
    global player
    print("HackingSystem v1.3")
    while True:
        if player.curSystemPort == None:
            action = input(f"[{player.curSystemIp}/home~]>")
        else:
            action = input(f"[{player.curSystemIp}/{player.curSystemPort}~]>")
        
        if action.startswith("scan"):
            if "-s" in action:
                for x in player.formatGetServers():
                    print('-'*20)
                    print(f'Name:{x["name"]}\nIP:{x["ip"]}\nHackLvl:{x["hackLvl"]}\nRoot access:{x["root"]}')
                    print()
            if "-n" in action and player.curSystemIp != "0.0.0.0":
                for x in player.formatGetNodes():
                    
                    print(f'Name:{x["name"]} \n    HackLvl:{x["hackLvl"]} \n    Port:{x["port"]} \n    Hacked:{x["hacked"]}')
        if action.startswith("get -root"):
            serverip = action.split()[2]
            response = player.gainServerRoot(serverip)
            if response:
                print(f"Gained root on ({serverip}) and entered the server")
            else:
                print(f'Failed for a reason :(')
        
        if action.startswith("take") and "-n" in action and player.curSystemIp != "0.0.0.0":
            nodePort = action.split()[3] # 4th element: exaple command take <-n>#node <-m>#money <port>
            mode = action.split()[2]
            if mode == "-m":
                amoGain = player.stealNodeMoney(nodePort)
                if amoGain != None:
                    print(F'You gained ${round(amoGain, 2)} from {player.curSystemIp}/{nodePort}')
                    player.money += round(amoGain, 2)

            else:
                amoGain = player.stealNodeSkill(nodePort)
                if amoGain != None:
                    print(F'You Gained {round(amoGain, 2)} skill points from [{player.curSystemIp}/{nodePort}]')
                    player.hackLvl += round(amoGain, 2)

        if action.startswith("player") and "-i" in action:
            print(F'   Name:{player.name} \n   Money:{player.money} \n   HackLvl:{player.hackLvl}')    
        if action.startswith("connect -s"):
            serverip = action.split()[2]
            response = player.enterServer(serverip)
            if response:
                print(f"Connected to ({serverip})")

        elif action.startswith("connect") and "-h" in action:
            player.exitServers()
            print("Returned to local machine")

        if action == "clear" or action == "cls" or "-C" in action:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("HackingSystem v1.3")


if __name__ == "__main__":
    if not testing:
        print(True)
        t1 = threading.Thread(target=main)
        t1.start()
    else:
        t1 = threading.Thread(target=test)
        t1.start()