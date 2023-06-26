import os
import sys
import random
import string
import ctypes
from uniref import WinUniRef #Importing Uniref Library for init KINGDOMS :D
import dearpygui.dearpygui as b
def GetRandomString():
    j = string.ascii_letters + string.ascii_uppercase
    return (''.join(random.choice(j) for x in range(12)))
def SetConsTitle():
    return ctypes.windll.kernel32.SetConsoleTitleW(GetRandomString()) #SetConsoleTitleA in ANSI Type, SetConsoleTitleW in UNICODE Type :D
class Kingdoms():
    def GetProcess():
        ref = WinUniRef("Kingdoms.exe")
        return ref 
    def GetPID():
        l = Kingdoms
        return l.GetProcess().pid #Getting PID Process :D
    class Player_Parameters(): #Player_Parameters.cs :D
        def SetCustomPoints(old_value: int, new_value: int):
            x = Kingdoms
            get_playerparam_image = x.GetProcess().find_class_in_image("Assembly-CSharp", "Player_Parameters") #Current Player
            hj = get_playerparam_image.find_field("Points_To_Learn") #We Don't Know a REAL Address, but you can find REAL Value(40 for example)
            mz = get_playerparam_image.guess_instance_address() 
            for z in mz:
                hj.instance = z
                if(hj.value == old_value):
                    hj.instance = z
                    print(f"Address: {hex(hj.instance)}")
                    hj.value = new_value
                    print(f"Value: {hj.value}")

def PrintPID():
    print(f"PID: {str(Kingdoms.GetPID())}")
def SetPoints():
    Kingdoms.Player_Parameters.SetCustomPoints(40, 1500)
class DPG():
    def InitDearPygui():
        b.create_context()
        with b.font_registry():
            nimbus = b.add_font(os.getcwd() + "\\Font\\NimSans.ttf", 13)
        with b.window(label="KINGDOMS Trainer by PyoKioto", width=455, height=455, no_collapse=True, no_close=True) as wx:
            b.add_button(label="Unlimited Points", width=155, height=155, callback=SetPoints)
            b.bind_font(nimbus)
        b.create_viewport(title=GetRandomString(), width=455, height=455, resizable=False, decorated=False)
        b.setup_dearpygui()
        b.show_viewport()
        b.start_dearpygui()
        b.destroy_context()
if __name__ == "__main__":
    SetConsTitle()
    DPG.InitDearPygui()
