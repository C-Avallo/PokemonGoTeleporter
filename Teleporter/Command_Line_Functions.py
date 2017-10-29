import os
import time
import Loading_Bar
import pymsgbox
import Notifaction
import sys

print("Loaded Command Line Functions")

directory = None
projectDirectory = None

def show_loading_info():
    print("Warning - No movement while using this 'hack' within 100 seconds could result in GPS restart and a ban!")
def killChrome():
    os.system('pkill -f "Chrome"')
    print("Killed Chrome")
def chromeFront():
    print("Deactvated")
    #time.sleep(5)
    #os.system("osascript -e 'do shell script \"open -a Google\\\ Chrome \"'")
    #print("Brought Chrome to Front")
def update():
    os.system("osascript " + directory + "Run_Once.scpt")
    print("Running 1 iteration of auto-clicker")
def mirror():
    os.system("osascript " + directory + "IphoneMirror.scpt")
    print("Mirroring iPhone")
    Loading_Bar.doLoading_Bar(0, 20)
def say(to_say):
    os.system("say {}".format(str(to_say)))
    print("Said: " + str(to_say))
def run_app(path):
    print("Running Default Xcode Config")
    os.system("open {}".format(str(path)))
    print("Opened Xcode with Project: " + str(path))
    Loading_Bar.doLoading_Bar(0, 20)
    os.system("osascript " + directory + "Run_My_Iphone.scpt")
def run_auto_clicker():
    os.system("osascript " + directory + "Auto-Clicker.scpt")
    print("Running Auto-Clicker(K to Quit - Don't just close the process)")
def confirmXcode():
    buttons_xcode_confirm = ['Ok', 'No-Way']
    xcode_confirm_output = pymsgbox.confirm(text=('Run Auto-Xcode?'), title='Pokemon H@ck', buttons=buttons_xcode_confirm)
    if (xcode_confirm_output == buttons_xcode_confirm[0]):
        run_app(projectDirectory)
    elif (buttons_xcode_confirm == buttons_xcode_confirm[1]):
        print("Skipping Default Xcode Config")
def confirmMirror():
    buttons_mirror_config = ['Ok', 'No-Way']
    mirror_config = pymsgbox.confirm(text=('Run Screen Mirror?'), title='Pokemon H@ck', buttons=buttons_mirror_config)

    if (mirror_config == buttons_mirror_config[0]):
        mirror()
    elif (mirror_config == buttons_mirror_config[1]):
        print("Skipping Default Xcode Config")
